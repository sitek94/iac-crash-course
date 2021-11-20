# Infrastructure as Code

## Export bucket endpoint

```bash
~ pulumi stack output

Current stack outputs (2):
    OUTPUT           VALUE
    bucket_endpoint  http://my-bucket-a8b5dcb.s3-website.eu-central-1.amazonaws.com
    bucket_name      my-bucket-a8b5dcb
```

```bash
~ curl $(pulumi stack output bucket_endpoint)

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Hello IaC</title>
  </head>
  <body>
    <h1>Infrastructure as Code</h1>
  </body>
</html>
```
