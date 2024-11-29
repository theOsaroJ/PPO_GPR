from gpmodel_class import GPModel

prior_path = '../results/final_prior.csv'
test_path = '../dataset/unlabeled.csv'
batch_size= 1

model = GPModel(prior_path, test_path, batch_size)
model.update_model(None)

r2 = model.calculate_r2()
print(r2)

predictions_path= '../results/unlabeled_predictions.csv'
model.save_predictions(predictions_path)
