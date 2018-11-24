---
title: Creating Audio Driver Objects
description: Creating Audio Driver Objects
ms.assetid: c5d1b1b6-fc47-4227-bcca-1119488dce3b
keywords:
- audio driver objects WDK
- COM object creation WDK audio
- objects WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Audio Driver Objects


## <span id="creating_audio_driver_objects"></span><span id="CREATING_AUDIO_DRIVER_OBJECTS"></span>


In user mode, COM objects are created using a function such as **CoCreateInstance** (described in the Microsoft Windows SDK documentation), where the client is unaware of how the memory required for the object is allocated. In kernel mode, however, where the allocation of memory tends to be tightly controlled, a different method of object creation is necessary.

The audio driver model uses the concept of the COM interface, as defined by the **IUnknown** interface. Audio drivers, however, are not required to access the registry or to use mechanisms such as in-process servers. Miniport drivers are not required to support aggregation.

By convention, the function used to create a particular class of objects always takes the same form:

```cpp
NTSTATUS CreateMyObject(
   OUT PUNKNOWN  *Unknown,
   IN REFGUID ClassId,
   IN PUNKNOWN OuterUnknown OPTIONAL,
   IN POOL_TYPE PoolType
 );
```

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>*Unknown*  
Pointer to a pointer to an **IUnknown** interface. The function outputs a reference to the newly created object through *Unknown*.

<span id="ClassId"></span><span id="classid"></span><span id="CLASSID"></span>*ClassId*  
Specifies the class GUID, which is passed by reference. This parameter is used only if the function creates objects of multiple classes. Otherwise, it is set to **NULL**.

<span id="OuterUnknown"></span><span id="outerunknown"></span><span id="OUTERUNKNOWN"></span>*OuterUnknown*  
Specifies the **IUnknown** interface for aggregating the new object. This parameter can be set to **NULL** to indicate that no aggregation is required.

<span id="PoolType"></span><span id="pooltype"></span><span id="POOLTYPE"></span>*PoolType*  
Specifies the type of memory pool from which the object is to be allocated (see [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707)).

The first three parameters are identical to the parameters of the COM **CoCreateInstance** function. For an example of a creation function of this type, see the **CreateMiniportMidiFM** function in the Fmsynth sample audio driver in the Microsoft Windows Driver Kit (WDK).

Another convention is to supply a New*Xxx* function for a class. Such functions provide an easy way to instantiate (create and initialize) an object, as shown in the following example:

```cpp
NTSTATUS NewMyObject(
 OUT PMYINTERFACE  *InterfacePointer,
 IN PUNKNOWN  OuterUnknown OPTIONAL,
 IN POOL_TYPE  PoolType,
  // ...more parameters
 );
```

The NewMyObject function creates and initializes an object, and then passes a pointer back to the interface. Because the initialization parameters are class-specific, so is the prototype of a New*Xxx* function. The New*Xxx* function provides convenient access to the constructor for the object.

For an example of a New*Xxx* function of this type, see [**PcNewDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff537712).

 

 




