---
Description: 'Reference-Counting Conventions for COM Objects'
MS-HAID: 'audio.reference\_counting\_conventions\_for\_com\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Reference-Counting Conventions for COM Objects'
---

# Reference-Counting Conventions for COM Objects


## <span id="reference_counting_conventions_for_com_objects"></span><span id="REFERENCE_COUNTING_CONVENTIONS_FOR_COM_OBJECTS"></span>


The methods in the audio interfaces follow a general set of rules for counting references on the COM objects that they take as input parameters or return as output parameters. These rules, and their exceptions, are summarized below. For more information about COM interfaces, see the COM section of the Microsoft Windows SDK documentation.

### <span id="Reference_Counting_on_Input_Parameters"></span><span id="reference_counting_on_input_parameters"></span><span id="REFERENCE_COUNTING_ON_INPUT_PARAMETERS"></span>Reference Counting on Input Parameters

When calling a method that takes a reference to an object *X* as an input parameter, the caller must hold its own reference on the object for the duration of the call. This behavior is necessary to ensure that the method's pointer to object *X* remains valid until it returns. If the object *Y* that implements this method needs to hold a reference to object *X* beyond the return from this method, the method should call [**AddRef**](com.iunknown_addref) on object *X* before returning. When object *Y* later finishes using object *X*, it should call [**Release**](com.iunknown_release) on object *X*.

For example, the [**IServiceGroup::AddMember**](audio.iservicegroup_addmember) method calls [**AddRef**](com.iunknown_addref) on the [IServiceSink](audio.iservicesink) object that it adds to its service group. To complement this behavior, the [**IServiceGroup::RemoveMember**](audio.iservicegroup_removemember) method calls [**Release**](com.iunknown_release) on the IServiceSink object that it removes from the service group.

### <span id="Reference_Counting_on_Output_Parameters"></span><span id="reference_counting_on_output_parameters"></span><span id="REFERENCE_COUNTING_ON_OUTPUT_PARAMETERS"></span>Reference Counting on Output Parameters

A method that passes an object reference to the caller through an output parameter should call [**AddRef**](com.iunknown_addref) on the object before it returns (or before it releases its own reference to the object). This behavior is necessary to ensure that the caller holds a valid reference upon return from the call. The caller is responsible for calling [**Release**](com.iunknown_release) on the object when it has finished using it.

For example, the [**IMiniportWaveCyclic::NewStream**](audio.iminiportwavecyclic_newstream) method calls [**AddRef**](com.iunknown_addref) on the stream, service group, and DMA channel objects that it outputs to the caller (the WaveCyclic port driver). The caller is responsible for releasing these references when it no longer needs them. For an implementation of the **IMiniportWaveCyclic::NewStream** method that shows this behavior, see the Sb16 sample adapter in the Microsoft Windows Driver Kit (WDK).

### <span id="Exceptions_to_the_Rules"></span><span id="exceptions_to_the_rules"></span><span id="EXCEPTIONS_TO_THE_RULES"></span>Exceptions to the Rules

For a description of the unconventional reference counting that this method performs on its *DmaChannel* output parameter, see [**IMiniportWavePci::NewStream**](audio.iminiportwavepci_newstream).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Reference-Counting%20Conventions%20for%20COM%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



