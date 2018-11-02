---
title: Native Debugger Objects in NatVis
description: The dx command displays a C++ expression using the NatVis extension model. For more information about NatVis, see Create custom views of native objects in the debugger.
keywords: [Native Debugger Objects in NatVis"]
ms.author: domars
ms.date: 08/10/2017
ms.localizationpriority: medium
---

# Native Debugger Objects in NatVis

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

[Create custom views of native objects](https://msdn.microsoft.com/library/jj620914.aspx)

[Writing debugger type visualizers for C++ using .natvis files](https://code.msdn.microsoft.com/windowsdesktop/Writing-type-visualizers-2eae77a2)

[**.nvload**](-nvload--natvis-load-.md)

[**.nvlist**](-nvlist--natvis-list-.md)

[**.nvunload**](-nvunload--natvis-unload-.md)

[**.nvunloadall**](-nvunloadall--natvis-unload-all-.md)


## <span id="Custom_NatVis_object_example"></span><span id="custom_natvis_object_example"></span><span id="CUSTOM_NATVIS_OBJECT_EXAMPLE"></span>Custom NatVis object example


Create a simple C++ application that has an instance of the class **CDog**.

```cpp
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
<AutoVisualizer xmlns="https://schemas.microsoft.com/vstudio/debugger/natvis/2010">
   <Type Name="CDog">
      <DisplayString>{{Age = {m_age} years. Weight = {m_weight} pounds.}}</DisplayString>
   </Type>
</AutoVisualizer>
```

Copy Dog.natvis to the Visualizers folder in your installation directory for Debugging Tools for Windows. For example:

C:\\Program Files\\Debugging Tools for Windows (x64)\\Visualizers

Run your program, and break in at the main function. Take a step so that the variable `MyDog` gets initialized. Display `MyDog` using [**??**](----evaluate-c---expression-.md) and again using **dx**.

```dbgcmd
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
 






