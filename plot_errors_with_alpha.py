plt.plot(alphas, train_errors, label="training")
plt.plot(alphas, test_errors, label="testing")
plt.ylabel("Accuracy")
plt.xlabel("gammas")
plt.legend()
plt.show()