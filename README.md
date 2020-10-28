# flaskonacci

[Perfect subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem) with Fibonacci twist, build with Flask. Read task description [here](fibonacci2.pdf) 

## install

```
git clone https://github.com/marcinliebiediew/flaskonacci
cd flaskonacci
pip install pipenv
pipenv install
pipenv run flask create_db
```

## run

```
pipenv run flask run
```

## test

```
pipenv run pytest
```

## benchmark

```
pipenv run flask fib_benchmark
```

## dockerize

```
docker build -t flaskonacci:1 .
docker run -t flaskonacci:1
```
