## 网络拓扑解释  
  
- 攻击机kali: IP 172.17.0.4
- 靶机IDS   ：IP 172.17.0.3  
  
收集流量流程是：选择攻击方式——攻击机开始攻击，靶机`tcpdump`收集流量——靶机对`pcap`流量
  
### DDOS  
  
攻击机在使用nmap工具扫描靶机端口，获得redis服务运行的6379端口. 对此端口进行DDOS攻击，
记录流量文件`ddos.pcap`  
  
### nmap  
  
### arp-scan   
  
流量收集使用
  
```shell
arp-scan -l -r 5
```
