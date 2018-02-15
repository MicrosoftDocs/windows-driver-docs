---
title: .browse (Display Command in Browser)
description: The .browse command displays the output of a specified command in a new Command Browser window.
ms.assetid: 37822DDE-8AA8-4DB9-8213-08E73110ACE5
keywords: [".browse (Display Command in Browser) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .browse (Display Command in Browser)
api_type:
- NA
---

# .browse (Display Command in Browser)


The **.browse** command displays the output of a specified command in a new [Command Browser window](command-browser-window.md).

```
.browse Command
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*  
The command to be executed and displayed in a new Command Browser window.

Remarks
-------

The following example uses the **.browse** command to display the output of the [**.chain /D**](-chain--list-debugger-extensions-.md) command in a Command Browser window.

```
.browse .chain /D
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.browse%20%28Display%20Command%20in%20Browser%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




