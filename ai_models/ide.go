package main

import (
	"github.com/tensorflow/tensorflow/tensorflow/go"
)

func main() {
	// Create an intelligent IDE
	ide := tensorflow.NewIDE()
	// Add features to the IDE
	ide.AddFeature(tensorflow.NewCodeCompletionFeature())
	ide.AddFeature(tensorflow.NewGitControlFeature())
	// Compile the IDE
	ide.Compile()
}
