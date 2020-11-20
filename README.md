# GitSampleSurvey



## 良いエンジニアとは

* コミットした回数・行数が多い
* リポジトリ数
* githubのアカウントを登録した時期
* 人との会話が多い→githubでは数えれなさそう？
* Issueの数→多ければ放置している、少なければ良い、立てない人も



**活動力**

* どの程度コミットしているか
  * 今までの総合コミット数
    * マイページのコントリビューションを数える

**経験**

* パブリック、プライベートリポジトリ数がどの程度あるか
  * 総合リポジトリ数
    * https://api.github.com/user/68428305　で取得(認証が必要)

**発言力**

* プルリク=事業やコードの数
* zenn など他のサービスのapiも使う

* パブリック・プライベートリポジトリの差

**実装力**

* スター数→平均
  * 全リポジトリのスター数合計
    1. https://api.github.com/users/SakaiTaka23/repos でリポジトリ検索
    2. Stared_urlにアクセス

**継続力**

* リポジトリあたりのコミット数
  * それぞれのリポジトリのコミット数





## api

* 認証させる ヘッダー

  * Accept : application/vnd.github.v3+json

  * Authorization : token $token



**リポジトリ一覧**

パブリックのみ取得

https://api.github.com/users/SakaiTaka23/repos

研究室のリポジトリ取得？

https://api.github.com/user/repos

ユーザー情報　認証済みならプライベート情報も

https://api.github.com/users/SakaiTaka23

個人のプライベートリポジトリ取得

https://api.github.com/search/repositories?q=user:SakaiTaka23

**idからの取得**

idからユーザー情報取得

https://api.github.com/user/68428305

リポジトリ取得 パブリックのみ

https://api.github.com/user/68428305/repos

スター数

https://api.github.com/user/68428305/starred



## 現状の課題

* 何を基準とすれば良いかわからない
  * 100点のエンジニアといったものを基準としてそのどれくらいを達成しているか
* それ以外の考え方が思いつかない
* 少なくとも何だかの基準が必要



* ある程度仮定して進めることも必要？
  * 活発であれば実力も高い　など

