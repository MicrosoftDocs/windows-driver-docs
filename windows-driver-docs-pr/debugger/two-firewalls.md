---
title: Two Firewalls
description: Two Firewalls
ms.assetid: e6192cf8-02a4-4dbe-8ed7-a64f8efc24f6
keywords: ["remote debugging, two firewalls", "firewalls and remote debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Two Firewalls


## <span id="ddk_two_firewalls_dbg"></span><span id="DDK_TWO_FIREWALLS_DBG"></span>


In this scenario, you need to perform kernel debugging on a computer in Building A. Your technician is located in Building C, and he or she has access to symbols there. However, both buildings have firewalls that will not allow incoming connections.

You need to set up a repeater at a neutral site -- say, Building B. Then you can connect A outward to B, and connect C outward to B.

There will be four computers involved in this scenario:

-   The target computer, located in Building A.

-   The local host computer, located in Building A. This computer will run a KD connection server. It will be connected to the target computer by a debug cable or 1394 cable, and will connect outward to the repeater. Let this computer's IP address be 127.0.10.10.

-   The computer in Building B. This will run the repeater. Let its IP address be 127.0.20.20.

-   The computer in Building C where the technician is located. This computer will run WinDbg as a smart client. Let its IP address be 127.0.30.30.

First, make sure the target computer is configured for debugging and is attached to the local host computer. In this example, a 1394 cable is used.

Second, start the repeater on 127.0.20.20:

``` syntax
dbengprx -p -s tcp:port=9001 -c tcp:port=9000,clicon=127.0.10.10 
```

Third, start the KD connection server on 127.0.10.10 in Building A as follows:

``` syntax
kdsrv -t tcp:port=9000,clicon=127.0.20.20,password=longjump 
```

Finally, start the smart client on 127.0.30.30 in Building C. (This can actually be done before or after starting the server in Building A.)

``` syntax
windbg -k kdsrv:server=@{tcp:server=127.0.20.20,port=9001,password=longjump},trans=@{1394:channel=9} -y SymbolPath
```

### <span id="five_computer_scenario"></span><span id="FIVE_COMPUTER_SCENARIO"></span>Five-Computer Scenario

This scenario can be made even more complicated if you suppose that the symbols are on one computer in Building C, but the technician is at a different computer.

Suppose that 127.0.30.30 has the symbols, as before, and that its local name is \\\\BOXC. The smart client can be started with the same command as above but with an additional **-server** parameter. Since no one will be using this machine, it will take less processing time if you use KD instead of WinDbg:

``` syntax
kd -server npipe:pipe=randomname -k kdsrv:server=@{tcp:server=127.0.20.20,port=9001,password=longjump},trans=@{1394:channel=9} -y SymbolPath
```

Then the technician, elsewhere in the building, can start a debugging client as follows:

``` syntax
windbg -remote npipe:server=\\BOXC,pipe=randomname 
```

Notice that the password must be supplied by the first non-repeater in the chain (the smart client on \\\\BOXC), not by the final debugger in the chain.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Two%20Firewalls%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




