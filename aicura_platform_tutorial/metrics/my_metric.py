from cbdf_api import Metric

class MyMetric(Metric):
    def __init__(self, n_classes:int=2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_classes = n_classes

    def get_metric(self):
        return mean_per_class_accuracy(self.n_classes)

# calculates per class the True-positive/class_instances and averages all of these
def mean_per_class_accuracy(n_classes):
    @tf.function
    def mpca(y_true, y_pred):
        class_accuracies = []
        for i in range(0, n_classes):
            class_indexes = tf.where(math_ops.equal(math_ops.argmax(y_true, axis=-1), i))
            true = tf.gather_nd(math_ops.argmax(y_true, axis=-1), class_indexes)
            pred = tf.gather_nd(math_ops.argmax(y_pred, axis=-1), class_indexes)
            class_accuracy = tf.reduce_mean(math_ops.cast(math_ops.equal(true, pred), K.floatx()))
            class_accuracies.append(class_accuracy)
        return tf.reduce_mean(class_accuracies)

    return mpca
