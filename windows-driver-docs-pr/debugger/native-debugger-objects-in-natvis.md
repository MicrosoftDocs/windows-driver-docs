---
title: Native Debugger Objects in NatVis
description: The dx command displays a C++ expression using the NatVis extension model. For more information about NatVis, see Create custom views of native objects in the debugger.
keywords: ["dx (Display Debugger Object Model Expression) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 08/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Objects in NatVis

## Overview

Native debugger objects represent various constructs and behaviors of the debugger environment. Example debugger objects include the following.

-   Session
-   Threads / Thread
-   Processes / Process
-   Stack Frames / Stack Frame
-   Local Variables
-   Modules / Module
-   Utility
-   State
-   Settings

You can use the dx command and LINQ to interact with the debugger objects. For more informaton, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) and [Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md).

You can also work with debugger objects using JavaScript. For more information about that see, 
[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

This topic describes how you can create custom NatVis visualizers to display debugger objects. 

## NatVis Development Resources

Refer to these resources for general information about working with NatVis.

[Create custom views of native objects](http://msdn.microsoft.com/library/jj620914.aspx)

[Writing debugger type visualizers for C++ using .natvis files](http://code.msdn.microsoft.com/windowsdesktop/Writing-type-visualizers-2eae77a2)

[**.nvload**](-nvload--natvis-load-.md)

[**.nvlist**](-nvlist--natvis-list-.md)

[**.nvunload**](-nvunload--natvis-unload-.md)

[**.nvunloadall**](-nvunloadall--natvis-unload-all-.md)


## <span id="Custom_NatVis_object_example"></span><span id="custom_natvis_object_example"></span><span id="CUSTOM_NATVIS_OBJECT_EXAMPLE"></span>Custom NatVis object example


Create a simple C++ application that has an instance of the class **CDog**.

```ManagedCPlusPlus
class CDog
{
public:
   CDog(){m_age = 8; m_weight = 30;}
   long m_age;
   long m_weight;
};

int main()
{
   CDog MyDog;
   printf_s("%d, %d\n", MyDog.m_age, MyDog.m_weight);
   return 0;
}
```

Create a file named Dog.natvis that contains this XML:

```XML
<?xml version="1.0" encoding="utf-8"?>
<AutoVisualizer xmlns="http://schemas.microsoft.com/vstudio/debugger/natvis/2010">
   <Type Name="CDog">
      <DisplayString>{{Age = {m_age} years. Weight = {m_weight} pounds.}}</DisplayString>
   </Type>
</AutoVisualizer>
```

Copy Dog.natvis to the Visualizers folder in your installation directory for Debugging Tools for Windows. For example:

C:\\Program Files\\Debugging Tools for Windows (x64)\\Visualizers

Run your program, and break in at the main function. Take a step so that the variable `MyDog` gets initialized. Display `MyDog` using [**??**](----evaluate-c---expression-.md) and again using **dx**.

```
0:000> ??MyDog
class CDog
   +0x000 m_age        : 0n8
   +0x004 m_weight     : 0n30
0:000> *
0:000> dx -r1 MyDog
.....
MyDog     : {Age = 8 years. Weight = 30 pounds.} [Type: CDog]
```


## <span id="see_also"></span>See also

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

[Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md)

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md) 

 
---
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dx%20%28Display%20Debugger%20Object%20Model%20Expression%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





