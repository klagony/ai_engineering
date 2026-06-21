# AI ENGINEERING

## Model Choice
*Why this particular model was chosen?*
- **small size** under 4b paramethers as required
- **good performance** few shot promting improved the macro F1 score from 0.4 to 0.8
- **fine-tunning** https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/

## LoRA Hyperparameters
*Was hast Du variiert, was war der Effekt?*
### Hyperparamether tuning
- **LoRA Rank** Controls the number of trainable parameters in the LoRA adapter matrices. A higher rank increases model capacity but also memory usage.(r = 8, 16, 32)
- **LoRA Alpha** Scales the strength of the fine-tuned adjustments in relation to the rank (r or 2r)
- **LoRa Dropout** applies regularisation, by default sero, set 0.1 to add regularization  if model overfitts
- **Weight Decay** A regularization term that penalizes large weights to prevent overfitting and improve generalization. (0.01 (recommended) - 0.1)
- **Target modules** Specify which parts of the model you want to apply LoRA adapters to — either the attention `q_proj, k_proj, v_proj, o_proj`, the MLP `gate_proj, up_proj, down_proj`, or both.(recommended to target all)

## Overfitting
*Wie hast Du Overfitting erkannt bzw. verhindert? (Bei wenigen hundert Beispielen sehr real.)*

## Chat template and data formatting
*Chat-Template / Datenformat: Wie hast Du die Trainingsbeispiele formatiert, und warum ist Konsistenz zwischen Training und Inferenz hier kritisch?*


## Fine-tuning vs Promting
*Ergebnisvergleich: Wo gewinnt das Fine-Tuning, wo das Prompting? Deine Interpretation. Übertrag auf die Praxis: Wann würdest Du im Produktionskontext fine-tunen statt prompten - und wann ist Fine-Tuning die falsche Antwort?*

## Cost Estimation
*Kosten: Grobe Abschätzung GPU-Zeit fürs Training vs. Inferenzkosten/-latenz beider Ansätze.*