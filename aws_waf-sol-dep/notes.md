# WAF Solutin POC

## Install CLI

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip -y
unzip awscliv2.zip
sudo ./aws/install
sudo rm -rf aws awscliv2.zip
```

##  Install Poetry (Python)

```bash
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/home/ubuntu/.local/bin:$PATH"' >> /home/ubuntu/.bashrc
source ~/.bashrc
poetry --version
```

## Set Variables!!

```bash
export TEMPLATE_OUTPUT_BUCKET=koushal
export DIST_OUTPUT_BUCKET=kosuahl-2
export SOLUTION_NAME=waf-poc
export VERSION=1
export AWS_REGION=us-east-1
```