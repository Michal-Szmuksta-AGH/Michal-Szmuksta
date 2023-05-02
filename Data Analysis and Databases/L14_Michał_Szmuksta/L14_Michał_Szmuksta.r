# install.packages("magrittr")
library(magrittr)

# Exercise One
list <- 1:10
# print(list)
list %<>% log2() %>%
    sin() %>%
    sum() %>%
    sqrt() %>%
print(list)

data(iris)
print(head(iris))
aggr <- iris %>%
    aggregate(. ~ Species, ., mean)
print(aggr)

# Exercise 2
# install.packages("ggplot2")
library(ggplot2)
# install.packages("GGally")
library(GGally)

plott <- ggplot(iris, aes(x = Sepal.Width)) +
    geom_histogram(aes(fill=Species, color = Species), bins=20) +
    geom_vline(data=aggr, aes(xintercept=Sepal.Width, color=Species), linetype="dashed") +
    labs(x='x_axis', y='y_axis', title='title')
ggsave("/home/rplot.jpg", plot = plott)

plott <- ggpairs(data = iris, aes(color = Species))
ggsave("/home/rplot2.jpg", plot = plott)

# Exercise 3
# install.packages("cluster")
library(cluster)
x <- iris[, 1:4]

y <- iris[,5]

sum_sqr <- c()

for (i in 1:10){
    kmeans_result <- kmeans(x, i)
    sum_sqr <- append(sum_sqr, kmeans_result$tot.withinss)
}

plott <- ggplot(data.frame(iteration = 1:length(sum_sqr), value = sum_sqr), aes(x = iteration, y = sum_sqr)) +
    geom_line() 
    ggsave("/home/rplot3.jpg", plot = plott) 
    
kmeans_result <- kmeans(x, 3)
plott <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = kmeans_result$cluster)) + geom_point()
ggsave("/home/rplot4.jpg", plot = plott)

plott <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = Species)) + geom_point() 
ggsave("/home/rplot5.jpg", plot = plott)