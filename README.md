# AI ENGINEERING

## Model Choice
*Why this particular model was chosen?*
- **small size** under 4b paramethers as required
- **good performance** few shot promting improved the macro F1 score from 0.4 to 0.8
- **fine-tunning** https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/

## LoRA Hyperparameters
*Was hast Du variiert, was war der Effekt?*
- **Rank**
- **Target Modules**
- **Learning Rate**

## Overfitting
*Wie hast Du Overfitting erkannt bzw. verhindert? (Bei wenigen hundert Beispielen sehr real.)*

## Chat template and data formatting
*Chat-Template / Datenformat: Wie hast Du die Trainingsbeispiele formatiert, und warum ist Konsistenz zwischen Training und Inferenz hier kritisch?*


## Fine-tuning vs Promting
*Ergebnisvergleich: Wo gewinnt das Fine-Tuning, wo das Prompting? Deine Interpretation. Übertrag auf die Praxis: Wann würdest Du im Produktionskontext fine-tunen statt prompten - und wann ist Fine-Tuning die falsche Antwort?*

## Cost Estimation
*Kosten: Grobe Abschätzung GPU-Zeit fürs Training vs. Inferenzkosten/-latenz beider Ansätze.*