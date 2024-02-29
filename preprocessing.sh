git clone https://github.com/pytorch/serve.git

mkdir transformer_hf

cp -R serve/examples/Huggingface_Transformers/* transformer_hf/

rm -rf serve

pip install -r requirements.txt

# change setup_config.json

python Download_Transformer_models.py

# in Transformer_handler_generalized_neuron.py we should change  "ts.torch_handler.Transformer_handler_generalized" to "Transformer_handler_generalized"

torch-model-archiver --model-name ruBERT2sentiment_test --version 1.0 --serialized-file "/Users/a1kayda/Desktop/mle2sber/transformer_hf/rubert-tiny2-sentiment/pytorch_model.bin" --handler "/Users/a1kayda/Desktop/mle2sber/transformer_hf/Transformer_handler_generalized.py" --extra-files "/Users/a1kayda/Desktop/mle2sber/transformer_hf/rubert-tiny2-sentiment/config.json,/Users/a1kayda/Desktop/mle2sber/transformer_hf/rubert-tiny2-sentiment/tokenizer_config.json,/Users/a1kayda/Desktop/mle2sber/transformer_hf/rubert-tiny2-sentiment/special_tokens_map.json,/Users/a1kayda/Desktop/mle2sber/transformer_hf/setup_config.json,/Users/a1kayda/Desktop/mle2sber/transformer_hf/Seq_classification_artifacts/index_to_name.json"


mkdir model_store
mv ruBERT2sentiment_test.mar model_store/
torchserve --start --model-store model_store --models my_model=ruBERT2sentiment_test.mar --ncs

curl -X POST http://127.0.0.1:8080/predictions/my_model -T sample_text.txt