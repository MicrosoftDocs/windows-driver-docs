---
title: hidkd.hidtree
description: The hidkd.hidtree command displays a list of all device nodes that have a HID function driver along with their child nodes. 
ms.assetid: 50FD5526-3B0E-4585-BFFD-72ED363D007A
keywords: ["hidkd.hidtree Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- hidkd.hidtree
api_type:
- NA
---

# !hidkd.hidtree


The **!hidkd.hidtree** command displays a list of all device nodes that have a HID function driver along with their child nodes. The child nodes have a physical device object (PDO) that was created by the parent node's HID function driver.

```
!hidkd.hidtree
```

This screen shot shows an example of the output of the **!hidtree** command.

![output of the hidtree command](images/hidkd01.png)

O

In this example, there are two device nodes that have a HID function driver. A functional device object (FDO) represents the HID driver in those two nodes. The first FDO node has two child nodes, and the second FDO node has one child node. In the debugger output, the child nodes have the PDO heading.

**Note**  This set of device nodes does not form a tree that has a single root node. The device nodes that have HID function drivers can be isolated from each other.

 

When you are debugging a HID issue, the **!hidtree** is a good place to start, because the command displays several addresses that you can pass to other HID debugger commands. The output uses [Debugger Markup Language (DML)](debugger-markup-language-commands.md) to provide links. The links execute commands that give detailed information related to an individual device node. For example, you could get information about an FDO by clicking one of the [**!hidfdo**](-hidkd-hidfdo.md) links. As an alternative to clicking a link, you can enter a command. For example, to see detailed information about the first node in the preceding output, you could enter the command **!devnode 0xffffe00003b18d30**.

**Note**  The DML feature is available in WinDbg, but not in Visual Studio or KD.

 

## <span id="DLL"></span><span id="dll"></span>DLL


Hidkd.dll

## <span id="see_also"></span>See also


[HID Extensions](hid-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!hidkd.hidtree%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





