---
Description: Creating Audio Driver Objects
MS-HAID: 'audio.creating\_audio\_driver\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Creating Audio Driver Objects
---

# Creating Audio Driver Objects


## <span id="creating_audio_driver_objects"></span><span id="CREATING_AUDIO_DRIVER_OBJECTS"></span>


In user mode, COM objects are created using a function such as **CoCreateInstance** (described in the Microsoft Windows SDK documentation), where the client is unaware of how the memory required for the object is allocated. In kernel mode, however, where the allocation of memory tends to be tightly controlled, a different method of object creation is necessary.

The audio driver model uses the concept of the COM interface, as defined by the **IUnknown** interface. Audio drivers, however, are not required to access the registry or to use mechanisms such as in-process servers. Miniport drivers are not required to support aggregation.

By convention, the function used to create a particular class of objects always takes the same form:

```
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
Specifies the type of memory pool from which the object is to be allocated (see [**POOL\_TYPE**](kernel.pool_type)).

The first three parameters are identical to the parameters of the COM **CoCreateInstance** function. For an example of a creation function of this type, see the **CreateMiniportMidiFM** function in the Fmsynth sample audio driver in the Microsoft Windows Driver Kit (WDK).

Another convention is to supply a New*Xxx* function for a class. Such functions provide an easy way to instantiate (create and initialize) an object, as shown in the following example:

```
NTSTATUS NewMyObject(
 OUT PMYINTERFACE  *InterfacePointer,
 IN PUNKNOWN  OuterUnknown OPTIONAL,
 IN POOL_TYPE  PoolType,
  // ...more parameters
 );
```

The NewMyObject function creates and initializes an object, and then passes a pointer back to the interface. Because the initialization parameters are class-specific, so is the prototype of a New*Xxx* function. The New*Xxx* function provides convenient access to the constructor for the object.

For an example of a New*Xxx* function of this type, see [**PcNewDmaChannel**](audio.pcnewdmachannel).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Creating%20Audio%20Driver%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


