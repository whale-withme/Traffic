### 网络拓扑解释  
  
- 攻击机kali: IP 172.17.0.4
- 靶机IDS   ：IP 172.17.0.3  
  
收集流量流程是：选择攻击方式——攻击机开始攻击，靶机`tcpdump`收集流量——靶机对`pcap`流量进行slips处理.
处理的日志文件放在对应的文件夹下.
  
### DDOS  
  
攻击机在使用nmap工具扫描靶机端口，获得redis服务运行的6379端口. 对此端口进行DDOS攻击，
记录流量文件`ddos.pcap`  
  
### nmap  
  
### arp-scan   
  
流量收集使用，对比`alert.log`发现大致是1min内出现两次alert, 间隔在30s左右
  
```shell
# 积累更多的alert, 重复500次
arp-scan -l -r 5000
```
### DNS  

  来源[UNB dataset](https://www.unb.ca/cic/datasets/)  

  所有良性和攻击流量都是在受害者一侧使用TCPDump捕获的，并根据它们的时间戳进行标记。我们总共捕获了20.7MB、147.6MB和102.5MB的DNS数据包，分别用于重流量、轻流量和良性流量。  
 然后，我们应用我们开发的DNS特征提取器包从所有.PCAP文件中提取14个无状态和16个有状态特征。每对重状态、重无状态、轻状态和轻无状态的良性/攻击比率为**60/40**。具体在目录中已经分类好   

### normal  

  ctu收集的正常流量[ctu dataset](https://www.stratosphereips.org/datasets-normal)  
    
### IoT  
  
  收集到关于一些物联网设备的恶意流量，并不能检测出来
