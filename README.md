# 3-tier-python
3-tier-python is a demo for a 3 tier architecture project in docker/k8s

## What is it?

A simple example of a three tier (actually it's only two, a LB isn't really a front end BUT in this example it is) architecture.

Apps count their view pages, as well as a total (recorded in REDIS).

## Topology

```
               Load balancer
                    +
                    |
       +--------------------------+
       v            v             v
     APP1          APP2          APP3
       +            +             +
       +--------------------------+
                    |
                    v
                   REDIS
```

## Usage

```
docker-compose up -d --scale app=3
```

## K8S Usage

You first need Redis.
Install it from helm:

```
cat > redis_values.yaml << EOF
---
# metrics:
#  enabled: true
usePassword: false
EOF
helm install -f ./redis_values.yaml redis stable/redis
kubectl apply -f ./3-tier-python.yaml
```

## HELM usage


```
cat > redis_values.yaml << EOF
---
# metrics:
#  enabled: true
usePassword: false
EOF
helm install -f ./redis_values.yaml redis stable/redis
helm install app3tierpython ./app3tierpython
```

