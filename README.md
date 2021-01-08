# GitSampleSurvey



## 良いエンジニアの事前定義

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




## 調査中標本

* リポジトリ→リポジトリ数、総コミット数、スター数
  * リポジトリの名前を受け取りコミット数、スター数を受け取る
  * **リポジトリはフォークしたものは数えない**
* 今まで確認した総数、平均、中央値、偏差値



### 今現在の状況

* データは1セット100件とし、3セット集め、全てを合計したものもデータとして分析した
* 極端な値が一つだけありそれがあるかないかによって値は大きく変わり入れるかどうか悩んでいる→それどころか値が低いものを除けるべきかどうかも検討している



## 新たな調査



### 調査した内容

contributions：総コミット数

public repo：パブリックリポジトリの数　その人が持ち主になっているもののみ？

stars：取得したスター数

commits：行ったコミット数

pull requests：プルリクを出した回数

issues：持っているイシューの数

contribution：関わったリポジトリの数(持ち主不問)

followers：フォロワーの数

### 最終的な評価

A++,A+,A,A-,B+,B　に分けて評価する

### 今現在考慮すべきこと

それぞれの調査した値に関してどのような比率で換算するべきか

### 結果

ものすごくできる人を10人集めた。その中で平均値、中央値のブレが小さい場合その要素は良いエンジニアとしての定義に当てはまるのではないか？逆にブレが大きい場合その要素は良いエンジアとして要素として薄いと考えられる。

|               | 平均  | 中央値 | 標準偏差 |
| ------------- | ----- | ------ | -------- |
| contributions | 22002 | 16805  | 19272    |
| public repo   | 38    | 36     | 26       |
| stars         | 2763  | 1250   | 3964     |
| commits       | 11760 | 7300   | 12494    |
| pull requests | 1208  | 666    | 1592     |
| issues        | 483   | 322    | 461      |
| contribution  | 93    | 80     | 60       |
| followers     | 4273  | 2050   | 6072     |

#### それぞれの類似度

中央値÷平均のパーセンテージで計算

割合は 類似度÷534(類似度合計)

降順ソート済み

| 要素          | 類似度(%) | 全体に占める割合(%) |
| ------------- | --------- | ------------------- |
| public repo   | 95        | 18                  |
| contribution  | 86        | 16                  |
| contributions | 76        | 14                  |
| issues        | 67        | 13                  |
| commits       | 62        | 12                  |
| pull requests | 55        | 10                  |
| followers     | 48        | 9                   |
| stars         | 45        | 8                   |

### 考察

パブリックリポジトリの数やコントリビューション数は良いエンジニアの要素として大きな割合を占めるということがわかる。エンジニアを評価する際もこの値の割合を大きくして計算したい。



## 実装状況

* [x] contributions：総コミット数
* [x] public repo：パブリックリポジトリの数　その人が持ち主になっているもののみ？
* [x] stars：取得したスター数
* [x] pull requests：プルリクを出した回数
* [x] issues：持っているイシューの数
* [ ] contribution：関わったリポジトリの数(持ち主不問)
* [x] followers：フォロワーの数





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



必要になりそうな値

contributions：総コミット数

public repo：パブリックリポジトリの数　その人が持ち主になっているもののみ？

stars：取得したスター数

commits：行ったコミット数

pull requests：プルリクを出した回数

issues：持っているイシューの数

contribution：関わったリポジトリの数(持ち主不問)

followers：フォロワーの数



**contributions**

pythonで書いたものを使用

**public repo**

https://api.github.com/users/SakaiTaka23

→public_repos

**stars**

pythonで書いたものを使用

**commits**

pythonで書いたものを使用

**pull requests**

https://api.github.com/search/issues?q=+type:pr+user:SakaiTaka23&sort=created&order=asc

→total_count

**issues**

pythonで追加する

**contribution**



**followers**

https://api.github.com/users/SakaiTaka23

→followers



## 現状の課題

* 何を基準とすれば良いかわからない
  * 100点のエンジニアといったものを基準としてそのどれくらいを達成しているか
* それ以外の考え方が思いつかない
* 少なくとも何だかの基準が必要



* ある程度仮定して進めることも必要？
  * 活発であれば実力も高い　など



* ~~フォークしたもののは実力に入れる？~~→入れない



* 周りの値を使ってデータを取得できたがそれ以外のアクセスできない値(経験、発言力)は基準を作ることすらできず測定方法がわからない



* 完成形について この調査結果をapiとして実装し、毎日データを増やし続けるか、しないか、固定値として扱いLaravel上で全て処理するか

