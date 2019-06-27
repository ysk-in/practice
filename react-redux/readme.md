# Udemy「Modern React with Redux」のノート

https://www.udemy.com/react-redux/

# プロジェクトについて

## jsx

label つきの input と button を静的に表示するだけの単純なもの。  
React と JSX を使って，HTML を生成する方法について。  
Course11 ～ 23

## components

ブログの閲覧者コメント一覧のようなものを表示する。  
各コメントは共通フォーマットのため，Component 化(関数化)して再利用する。  
外部ライブラリとして Semantic UI と Faker を利用する。  
Course25 ～ 40

## seasons

HTML 参照者の緯度(Latitude)と月(1 ～ 12 月)を取得し，夏か冬かを表示する。  
緯度と月が取得し終わるまでは Loading 画面を表示し，夏/冬が判定できたら適切な画面へ遷移させる動的なもの。  
Class を用いた Component 化を利用する。  
Course45 ～ 71

## pics

検索窓(type=text の input) に入力された言葉に該当する画像を表示する。  
input への入力を onChange イベントで state に保持する。  
その input を含む form が submit されたら(検索窓で Enter されたら)，onSubmit イベントでstateに設定された言葉に該当する画像を取得する処理を実行する。  
画像を取得する処理は，UnsplashAPI を axios で実行することで実現する。

# Component のライフサイクル

constructer -> render  
 -(render で return した Content がスクリーン表示)-> componentDidMount ->  
 -(rerender/update されたら)-> componentDidUpdate ->  
 -(Component が表示されなくなったら)-> componentWillUnmount

詳細は Course58

# イベントハンドラに指定する関数名について

イベントハンドラのコールバックに指定する関数の関数名は以下が一般的らしい。  
"on" + 要素名(Input など) + イベント種別(Change)  
例えば次のような感じ。`<input type="text" onChange={this.onInputChange} />`  
Course79

# イベントハンドラから起動されるメソッドの this について

イベントハンドラに以下のような方法でメソッドを指定する場合

```
class SearchBar extends React.Component {
  state = { term: "" };

  onFormSubmit() {
    event.preventDefault();
    console.log(this.state.term);
  };

  render() {
    return (
      ...(formの前後は省略)
      <form onSubmit={this.onFormSubmit}>
    );
  }
}
```

`console.log(this.state.term);`は this.state.term を log せず  
TypeError: Cannot read property 'state' of undefined のエラーを発生させる。  
これは，ここで this が undefined のため。

onSubmit に this.onFormSubmit を指定することでコールバックさせるが  
この方法だと this は undefined になってしまうらしい。  
対策は色々あるらしいが，ここでは 3 つの方法を紹介してくれた。

1. constructor でメソッドを bind(this)したもので上書きする

   ```
   class SearchBar extends React.Component {
     state = { term: "" };

     constructor() {
       super();
       this.onFormSubmit = this.onFormSubmit.bind(this);
     }
   ```

   古くからあるコードでよく使われている対策らしい。

1. (Babel 利用) メソッド定義でアロー関数を使う

   ```
   onFormSubmit = event => {
    event.preventDefault();

    console.log(this.state.term);
   };
   ```

   メソッド定義時にアローファンクションを使うことで対策できる。  
   ただし Babel に依存する書き方なので Babel が使える場合でのみ適用可能。

1. コールバックの指定にアロー関数を使う

   ```
    render() {
      return (
        ...(formの前後は省略)
        <form onSubmit={(e) => this.onFormSubmit(e)}>
    );
   }
   ```

   これでコールバックに this.onFormSubmit(e)メソッドを実行するだけの関数を定義・指定することができる。  
   onFormSubmit メソッドは this を介して実行されるため対策できる。

詳細は Course85(と 84, 92(thisが想定外 の別ケース))を参照
