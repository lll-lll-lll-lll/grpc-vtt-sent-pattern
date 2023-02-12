# grpc-vtt-sent-pattern


## Bidirectional streaming RPC方式を採用
- vttを解析するサービスがクライアントで、構文解析する側サービスがサーバー
- クライアントからは複数回文章を区切りながら構文解析のリクエストを送るため


### 設計
- 構文解析 -> サーバ側
- vtt字幕ファイル整形 -> クライアント側



# Ref 
- https://dev.to/techschoolguru/upload-file-in-chunks-with-client-streaming-grpc-golang-4loc