# mle2sber

This repo contain backend for telegram-bot and serving model for sentiment analysis with TorchServe


It perfectly works for MacOS 14.3.1 with Apple M1 Silicon (on CPU)

If you have Intel Silicon or GPU you can try use different image for serving (in .yml)

I already have Docker Desktop, so for monitoring and executing inside containers I use GUI

## How to use:

I use sentiment bert from <href>https://huggingface.co/seara/rubert-tiny2-russian-sentiment</href>, you can also manually download it to 'rubert-tiny2-sentiment' directory

#### in local terminal directory mle2sber

    docker-compose build
    
    docker-compose up

#### in serving docker exec

#### creating .mar from model (we have it locally and mount volume)

      torch-model-archiver --model-name ruBERT2sentiment_test --version 1.0 --serialized-file "/home/model-server/transformer_hf/rubert-tiny2-sentiment/pytorch_model.bin" --handler "/home/model-server/transformer_hf/Transformer_handler_generalized.py" --extra-files "/home/model-server/transformer_hf/rubert-tiny2-sentiment/config.json,/home/model-server/transformer_hf/rubert-tiny2-sentiment/tokenizer_config.json,/home/model-server/transformer_hf/rubert-tiny2-sentiment/special_tokens_map.json,/home/model-server/transformer_hf/setup_config.json,/home/model-server/transformer_hf/index_to_name.json"

#### in local terminal

#### register model

    curl -X POST "localhost:8081/models?model_name=ruBERT2sentiment_test&url=ruBERT2sentiment_test.mar&initial_workers=4"

#### if we want to increase num of workers

    curl -v -X PUT "http://localhost:8081/models/ruBERT2sentiment_test?min_worker=8"  

#### we can manually check our model with sample text

    curl -X POST http://127.0.0.1:8080/predictions/ruBERT2sentiment_test -T sample_text.txt
