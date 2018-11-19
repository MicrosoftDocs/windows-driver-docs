---
title: Reference-Counting Conventions for COM Objects
description: Reference-Counting Conventions for COM Objects
ms.assetid: e6b19110-37e2-4d23-a528-6393c12ab650
keywords:
- COM object references WDK audio
- object references WDK audio
- counting references WDK audio
- reference counts WDK audio
- input parameter reference counting WDK audio
- output parameter reference counting WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reference-Counting Conventions for COM Objects


## <span id="reference_counting_conventions_for_com_objects"></span><span id="REFERENCE_COUNTING_CONVENTIONS_FOR_COM_OBJECTS"></span>


The methods in the audio interfaces follow a general set of rules for counting references on the COM objects that they take as input parameters or return as output parameters. These rules, and their exceptions, are summarized below. For more information about COM interfaces, see the COM section of the Microsoft Windows SDK documentation.

### <span id="Reference_Counting_on_Input_Parameters"></span><span id="reference_counting_on_input_parameters"></span><span id="REFERENCE_COUNTING_ON_INPUT_PARAMETERS"></span>Reference Counting on Input Parameters

When calling a method that takes a reference to an object *X* as an input parameter, the caller must hold its own reference on the object for the duration of the call. This behavior is necessary to ensure that the method's pointer to object *X* remains valid until it returns. If the object *Y* that implements this method needs to hold a reference to object *X* beyond the return from this method, the method should call [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on object *X* before returning. When object *Y* later finishes using object *X*, it should call [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on object *X*.

For example, the [**IServiceGroup::AddMember**](https://msdn.microsoft.com/library/windows/hardware/ff536996) method calls [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on the [IServiceSink](https://msdn.microsoft.com/library/windows/hardware/ff537006) object that it adds to its service group. To complement this behavior, the [**IServiceGroup::RemoveMember**](https://msdn.microsoft.com/library/windows/hardware/ff537001) method calls [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on the IServiceSink object that it removes from the service group.

### <span id="Reference_Counting_on_Output_Parameters"></span><span id="reference_counting_on_output_parameters"></span><span id="REFERENCE_COUNTING_ON_OUTPUT_PARAMETERS"></span>Reference Counting on Output Parameters

A method that passes an object reference to the caller through an output parameter should call [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on the object before it returns (or before it releases its own reference to the object). This behavior is necessary to ensure that the caller holds a valid reference upon return from the call. The caller is responsible for calling [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on the object when it has finished using it.

For example, the [**IMiniportWaveCyclic::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536723) method calls [**AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) on the stream, service group, and DMA channel objects that it outputs to the caller (the WaveCyclic port driver). The caller is responsible for releasing these references when it no longer needs them. For an implementation of the **IMiniportWaveCyclic::NewStream** method that shows this behavior, see the Sb16 sample adapter in the Microsoft Windows Driver Kit (WDK).

### <span id="Exceptions_to_the_Rules"></span><span id="exceptions_to_the_rules"></span><span id="EXCEPTIONS_TO_THE_RULES"></span>Exceptions to the Rules

For a description of the unconventional reference counting that this method performs on its *DmaChannel* output parameter, see [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735).

 

 




