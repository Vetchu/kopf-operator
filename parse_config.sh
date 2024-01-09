kubectl create configmap cfmap --from-file=config.txt --dry-run=client -o yaml > configmap.yaml
kubectl apply -f configmap.yaml