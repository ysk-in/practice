# Udemy「Modern React with Redux」のノート

https://www.udemy.com/react-redux/

# React Redux 開発ツール

## デバッグツール redux-devtools-extension

Action の呼び出し履歴や State の遷移を参照  
https://github.com/zalmoxisus/redux-devtools-extension

以下の Course で紹介  
Course 223. Using Redux Dev Tools to Inspect the Store  
Course 224. Debug Sessions with Redux Dev Tools

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
その input を含む form が submit されたら(検索窓で Enter されたら)，onSubmit イベントで state に設定された言葉に該当する画像を取得する処理を実行する。  
画像を取得する処理は，UnsplashAPI を axios で実行することで実現する。

また，表示する画像を並べるのに grid を用いる。  
UnsplashAPI で取得した画像の clientHeight を動的に取得し css(grid のオプション)を指定する。

pics で学んだことのまとめを Course 107 でしてくれている。

## videos

pics と似たもの。pics で学んだことのおさらいが主目的。

## songs

Redux/React-Redux を state 管理に用いる

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

詳細は Course85(と 84, 92(this が想定外 の別ケース))を参照

# index.js の import について

`import actions from "../actions";`これで../actions/index.js が import される。  
Webpack により，ファイル名を指定しない場合，デフォルトで index.js が参照されるため。

# Array(配列)の複製

`[...oldListOfClaims, action.payload]` ES2015 で追加された記法で，元の配列 oldListOfClaims は変えず，新しい配列「oldListOfClaims の全要素+action.payload」を作ることができる。

> MDN リファレンス スプレッド構文  
> https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Spread_syntax#Spread_in_array_literals

詳細は Course135 (5:00 あたり) 参照

# Array(配列)から特定の要素を取り除く

```
const numbers = [1,2,3];
numbers.filter(numb => numb !== 2);
```

配列から 2 の要素が取り除かれたものが返る。

# Redux Cycle

ActionCreator -> Action -> Dispatch -> Reducers -> State

# Redux(ActionCreate) で非同期処理

まず，Provider の プロパティ store に ミドルウェア redux-thunk を指定する。

```
import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

ReactDOM.render(
  <Provider store={createStore(reducers, applyMiddleware(thunk))}>
```

次に，ActionCreate で Function を return する(`const fetchPosts = () => {...}`)。

```
export const fetchPosts = () => async dispatch => {
  const response = await jsonPlaceholder.get("/posts");
  dispatch({ type: "FETCH_POSTS", payload: response.data })
};
```

ActionCreate で Function を return すると，ミドルウェア redux-thunk が戻り値を Handle(\*1) する。  
\*1: redux-thunk は ActionCreate が Function を return すると dispatch を引数に関数を実行し，Function 以外を return すると戻り値を素通り(Redux?にそのまま渡す)させる。

redux-thunk は dispath を引数に関数を実行してくるため，非同期処理の完了を待ち自前で dispatch を実行することで，Redux の ActionCreate で非同期処理を実行が可能。

# 関数の実行結果をキャッシュ lodash#memoize

https://lodash.com/docs/4.17.15#memoize  
lodash の memorize で Function をラップすることで，同じ引数で Function が実行された場合は前回と同じ return をキャッシュから取得が可能。

詳細は 184. Memoizing Functions 参照

# Redux の ActionCreate で loadsh#memoize を使う

引数 id を受け 対応する User を情報を REST で取得する ActionCreate の fetchUser。

```
export const fetchUser = id => async dispatch => {
  const response = await jsonPlaceholder.get(`/users/${id}`);
  dispatch({ type: "FETCH_USER", payload: response.data })
};

```

過去に実行された id の場合は REST 実行せずにキャッシュから return したい。

このとき，fetchUser が参照する関数に直接 memoize を適用(`export const fetchUser = _.memoize(id) => async dispatch => {`)すると，参照先の関数(REST を実行し dispatch する処理)がキャッシュされるだけで，Redux は相変わらず関数(REST を含む処理)を実行してしまう。

意図通りにするためには，内部関数を作成し，それを memoize する。

```
export const fetchUser = id => dispatch => _fetchUser(id, dispatch);
const _fetchUser = _.memoize(async (id, dispatch) => {
  const response = await jsonPlaceholder.get(`/users/${id}`);
  dispatch({ type: "FETCH_USER", payload: response.data })
});
```
