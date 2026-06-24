# AI ENGINEERING

## Model Choice
*Why this particular model was chosen?*
- **small size** under 4b paramethers as required
- **good performance** few shot promting improved the macro F1 score from 0.4 to 0.8
- **fine-tunning potential** the model shows strong responsivness to fine-tuning in the benchmarks
source: https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/

## LoRA Hyperparameters
*What paramethers were varied and how it is affected performance?*
### Hyperparamether tuning
- **LoRA Rank** Controls the number of trainable parameters in the LoRA adapter matrices. A higher rank increases model capacity but also memory usage.(r = 4, 8, 16, 32)
- **LoRA Alpha** Scales the strength of the fine-tuned adjustments in relation to the rank (r or 2r)
- **LoRa Dropout** applies regularisation, by default sero, set 0.1 to add regularization to improve genralization (when model overfitts)
- **Weight Decay** A regularization term that penalizes large weights to prevent overfitting and improve generalization. (0.01 (recommended) - 0.1)
- **Target modules** Specify which parts of the model you want to apply LoRA adapters to — either the attention `q_proj, k_proj, v_proj, o_proj`, the MLP `gate_proj, up_proj, down_proj`, or both.(recommended to target all)
sources: https://app.readytensor.ai/lessons/lora-hyperparameter-tuning-analyzing-systematic-fine-tuning-experiments-x6R3aGoq; https://arxiv.org/pdf/2106.09685

## Overfitting
*How have you identified overfitting?*
- no overfitting (low trainig loss correspons to high accuracy/f1score on test dataset)
- normaly can be idetlified on training and validation loss discripancy (the val dataset were not created here)

## Chat template and data formatting
*How you formated the training examles?Is the consistency between training and interference*
- used `apply_chat_template` to ensure consistency
- if the format differs during interference, the model may not interpret the input correctly, leading to degraded performance

## Fine-tuning vs Promting
*When does fine-tuning wins, when promting?*
- fine-tuning: well defined task, a lot of specialized training data, high compute is available
- promting: few or no labeled examples, quick prototyping

## Cost Estimation
*Comparison of the GPU time for training and interference*
|Criteria/Method |Zero-shot promting |Few-Shot promting| LoRA Finetung(r=4, q+v, 1 epoch)| LoRA(r=16, q+v+k+o, 1 epoch )|LoRa(r=16, all, 3 epochs, regularization) |
|----------------|-------------------|-----------------|--------------------------------|-------------------------------|------------------------------------------|
|Accuracy        |        0.46       |      0.83       |        0.86                    |         0.91                  |                  0.90                    |
|Macro-F1        |        0.42       |      0.84       |        0.86                    |         0.91                  |                  0.90                    |
|Training time   |         0         |       0         |       8min45s                  |       9min18s                 |                22min26s                  |
|Interference time|       2min5s     |    2min58s      |        2min                    |       1min48s                 |                1min24s                   |