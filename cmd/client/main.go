package main

import (
	"context"
	"fmt"
	"log"
	"os"

	pb "github.com/lll-lll-lll-lll/grpc-vtt-sentpattern/cmd/client/api"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

var conn *grpc.ClientConn

func init() {
	var err error
	address := "[::]:50051"
	fmt.Println("start gRPC Client.")
	conn, err = grpc.Dial(
		address,

		grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithBlock(),
	)
	if err != nil {
		log.Fatal("Connection failed.")
	}
}

func main() {
	text := os.Args[1]
	if text == "" {
		fmt.Println("input text is empty")
		return
	}
	defer conn.Close()
	client := pb.NewVTTSentPatternServiceClient(conn)
	req := &pb.GetPatternRequest{Text: text}
	res, err := client.GetPattern(context.Background(), req)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(res)
}
