# scriptタグによるReact呼び出し
index.htmlに以下のsciprtタグを追加しReactを読み込む。    
```
<script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
```

```<script src="like_button.js"></script>```で，Reactを利用するJavaScriptを追加。  

like_button.jsで，```document.querySelectorAll(".like_button_container").forEach(domContainer ...(省略)```により，index.htmlのdivタグのclass=like_button_container(```<div class="like_button_container" data-commentid="1"></div>```など)を変数domContainerに設定。  

```ReactDOM.render(e(LikeButton, { commentID: commentID }), domContainer);```で，domContainerがLikeButton#renderに従い書き換えられる。  
