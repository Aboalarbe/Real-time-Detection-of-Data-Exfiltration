# Detection of data exfiltration via DNS in Realtime

implementation of a binary classifier aiming at predicting data exfiltration via DNS from a data stream (local Kafka Server).

## Introduction

While originally not intended for data transfer, the Domain Name System (DNS) is currently used to this end anyway, in a process called DNS tunneling (DNST). Malicious
users exploit DNST for data exfiltration from infected machines, posing a critical security threat. We train and evaluate state-of-the-art convolutional neural network, random forest, and ensemble classifiers to detect tunneling in DNS traffic. Finally, we assess the classifiers’ performance and robustness by exposing them to one day of real-traffic data.

## Feedback

If you have any feedback, please reach out at mhuss073@uottawa.ca

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.credential.net/profile/mohamedaboalarbe/wallet)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammed-elaraby/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Refrences

* https://www.unb.ca/cic/datasets/dns-exf-2021.html
* Malicious DNS Tunneling Detection in Real-Traffic DNS Data "Paper 1"
* Real-Time Detection of DNS Exfiltration and Tunneling from Enterprise Networks "Paper 2"
* Towards Comprehensive Detection of DNS Tunnels "Paper 3"
