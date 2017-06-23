import tensorflow as tf

# constants get intiated during run time

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)
node3 = tf.add(node1, node2)

# placeholder is a promise that that values will be replaced during runtime

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

# unlike constants variables dont get initiated
# they need to explicityly initalized

W = tf.Variable(1.0, tf.float32)
b = tf.Variable(0.0, tf.float32)
x = tf.placeholder(tf.float32)

linear_model = W * x + b
init = tf.global_variables_initializer()

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

optimiser = tf.train.GradientDescentOptimizer(0.01)
train = optimiser.minimize(loss)
session = tf.Session()
session.run(init)
for i in range(1000):
    session.run(train, {x: [1, 2, 3, 4], y: [1, 2, 1, 2]})

print(session.run([W, b]))
