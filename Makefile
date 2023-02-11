gen:
	protoc --go_out=./cmd/client --go_opt=paths=source_relative \
	--go-grpc_out=./cmd/client --go-grpc_opt=paths=source_relative \
	./api/api.proto \
	& \
	python -m grpc_tools.protoc -I ./ --python_out=./cmd/server  --grpc_python_out=./cmd/server api/api.proto