---
title: .dml_flow (Unasemmble with Links)
description: The .dml_flow command displays a disassembled code block and provides links that you can use to construct a code flow graph.
ms.assetid: 32B50228-05A5-4BA7-88B1-54D4E502EB85
keywords: [".dml_flow (Unasemmble with Links) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .dml_flow (Unasemmble with Links)
api_type:
- NA
---

# .dml\_flow (Unasemmble with Links)


The **.dml\_flow** command displays a disassembled code block and provides links that you can use to construct a code flow graph.

```
.dml_flow Start Target
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Start"></span><span id="start"></span><span id="START"></span>*Start*  
The address of an instruction from which the target address can be reached.

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>*Target*  
An address in the code block to be disassembled.

Remarks
-------

Consider the call stack shown in the following example.

```
0: kd> kL
Child-SP          RetAddr           Call Site
fffff880`0335c688 fffff800`01b41f1c nt!IofCallDriver
fffff880`0335c690 fffff800`01b3b6b4 nt!IoSynchronousPageWrite+0x1cc
fffff880`0335c700 fffff800`01b4195e nt!MiFlushSectionInternal+0x9b8
...
```

Suppose you want to examine all code paths from the start of **nt!MiFlushSectionInternal** to the code block that contains the return adress, `` fffff800`01b3b6b4 ``. The following command gets you started.

```
.browse .dml_flow nt!MiFlushSectionInternal fffff800`01b3b6b4
```

The output, in the [Command Browser window](command-browser-window.md), is shown in the following image.

![screen shot of .dml\-flow output](images/dmlflow01.png)

The preceding image shows the code block that contains the target address, `` fffff800`01b3b6b4 ``. There is only one link (`` fffff800`01b3b681 ``) at the top of the image. That indicates that there is only one code block from which the current code block can be reached. If you click the link, you will see that code block disassembled, and you will see links that enable you to further explore the code flow graph.

The two links at the bottom of the preceding image indicate that there are two code blocks that can be reached from the current code block.

## <span id="see_also"></span>See also


[Debugger Markup Language Commands](debugger-markup-language-commands.md)

[**uf (Unasemmble Function)**](uf--unassemble-function-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.dml_flow%20%28Unasemmble%20with%20Links%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





