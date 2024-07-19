package main

import (
	"github.com/tensorflow/tensorflow/tensorflow/go"
)

func main() {
	// Create a computer vision model
	model := tensorflow.NewModel()
	// Add layers to the model
	model.AddLayer(tensorflow.NewConv2DLayer())
	model.AddLayer(tensorflow.NewMaxPoolingLayer())
	// Compile the model
	model.Compile()
}
