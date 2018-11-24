---
title: IRQL annotations for drivers
description: When the driver code has IRQL annotations, the code analysis tools can make a better inference about the range of levels at which a function should run and can more accurately find errors.
ms.assetid: E4C1D490-BE06-483A-90E4-6F3223E269A3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRQL annotations for drivers

When the driver code has IRQL annotations, the code analysis tools can make a better inference about the range of levels at which a function should run and can more accurately find errors. For example, you can add annotations that specify the maximum IRQL at which a function can be called; if a function is called at a higher IRQL, the code analysis tools can identify the inconsistencies.

All driver developers must consider interrupt request levels (IRQLs). An IRQL is an integer between 0 and 31; PASSIVE\_LEVEL, DISPATCH\_LEVEL, and APC\_LEVEL are normally referred to symbolically, and the others by their numeric values. Raising and lowering the IRQL should follow strict stack discipline. A function should aim to return at the same IRQL at which it was called. The IRQL values must be non-decreasing in the stack. And a function cannot lower the IRQL without first raising it. IRQL annotations are intended to help enforce those rules.

When the driver code has IRQL annotations, the code analysis tools can make a better inference about the range of levels at which a function should run and can more accurately find errors. For example, you can add annotations that specify the maximum IRQL at which a function can be called; if a function is called at a higher IRQL, the code analysis tools can identify the inconsistencies.

Driver functions should be annotated with as much information about the IRQL that might be appropriate. If the additional information is available, it helps the code analysis tools in subsequent checking of both the calling function and the called function. In some cases, adding an annotation is a good way to suppress a false positive. Some functions, such as a utility function, can be called at any IRQL. In this case, having no IRQL annotation is the proper annotation.

When annotating a function for IRQL, it is especially important to consider how the function might evolve, not just its current implementation. For example, a function as implemented might work correctly at a higher IRQL than the designer intended. Although it is tempting to annotate the function based upon what the code actually does, the designer might be aware of future requirements, such as the need to lower maximum IRQL for some future enhancement or pending system requirement. The annotation should be derived from the intention of the function designer, not from the actual implementation.

You can use the annotations in the following table to indicate the correct IRQL for a function and its parameters. The IRQL values are defined in Wdm.h.

|IRQL annotation|Description|
|--- |--- |
|\_IRQL_requires_max_(_irql_)|The _irql_ is the maximum IRQL at which the function can be called.|
|\_IRQL_requires_min_(_irql_)|The _irql_ is the minimum IRQL at which the function can be called.|
|\_IRQL_requires_(_irql_)|The function must be entered at the IRQL specified by _irql_.|
|\_IRQL_raises_(_irql_)|The function exits at the specified _irql_, but it can only be called to raise (not lower) the current IRQL.|
|\_IRQL_saves_|The annotated parameter saves the current IRQL to restore later.|
|\_IRQL_restores_|The annotated parameter contains an IRQL value from _IRQL_saves_ that is to be restored when the function returns.|
|\_IRQL_saves_global_(kind, param)|The current IRQL is saved into a location that is internal to the code analysis tools from which the IRQL is to be restored. This annotation is used to annotate a function. The location is identified by kind and further refined by param. For example, OldIrql could be the kind, and FastMutex could be the parameter that held that old IRQL value.|
|\_IRQL_restores_global_(_kind_, _param_)|The IRQL saved by the function annotated with IRQL_saves_global is restored from a location that is internal to the Code Analysis tools.|
|\_IRQL_always_function_min_(_value_)|The IRQL value is the minimum value to which the function can lower the IRQL.|
|\_IRQL_always_function_max_(_value_)|The IRQL value is the maximum value to which the function can raise the IRQL.|
|\_IRQL_requires_same_|The annotated function must enter and exit at the same IRQL. The function can change the IRQL, but it must restore the IRQL to its original value before exiting.|
|\_IRQL_uses_cancel_|The annotated parameter is the IRQL value that should be restored by a DRIVER_CANCEL callback function. In most cases, use the IRQL_is_cancel annotation instead.|
 

## <span id="Annotations_for_DRIVER_CANCEL"></span><span id="annotations_for_driver_cancel"></span><span id="ANNOTATIONS_FOR_DRIVER_CANCEL"></span>Annotations for DRIVER\_CANCEL


There is a difference between the \_IRQL\_uses\_cancel\_ and \_IRQL\_is\_cancel\_ annotations. The \_IRQL\_uses\_cancel\_ annotation simply specifies that the annotated parameter is the IRQL value that should be restored by a DRIVER\_CANCEL callback function. The \_IRQL\_is\_cancel\_ annotation is a composite annotation that consists of \_IRQL\_uses\_cancel\_ plus several other annotations that ensure correct behavior of a DRIVER\_CANCEL callback utility function. By itself, the \_IRQL\_uses\_cancel\_ annotation is only occasionally useful; for example, if the rest of the obligations described by \_IRQL\_is\_cancel\_ have already been fulfilled in some other way.

|IRQL annotation|Description|
|--- |--- |
|IRQL_is_cancel|The annotated parameter is the IRQL passed in as part of the call to a DRIVER_CANCEL callback function. This annotation indicates that the function is a utility that is called from Cancel routines and that completes the requirements for DRIVER_CANCEL functions, including release of the cancel spin lock.|


## <span id="How_IRQL_Annotations_Interact"></span><span id="how_irql_annotations_interact"></span><span id="HOW_IRQL_ANNOTATIONS_INTERACT"></span>How IRQL Annotations Interact


IRQL parameter annotations interact with each other more than other annotations because the IRQL value is set, reset, saved, and restored by the various called functions.

### <span id="Specifying_Maximum_and_Minimum_IRQL"></span><span id="specifying_maximum_and_minimum_irql"></span><span id="SPECIFYING_MAXIMUM_AND_MINIMUM_IRQL"></span>Specifying Maximum and Minimum IRQL

The \_IRQL\_requires\_max\_ and \_IRQL\_requires\_min\_ annotations specify that the function should not be called from an IRQL that is higher or lower than the specified value. For example, when PREfast sees a sequence of function calls that do not change the IRQL, if it finds one with a \_IRQL\_requires\_max\_ value that is below a nearby \_IRQL\_requires\_min\_, it reports a warning on the second call that it encounters. The error might actually occur in the first call; the message indicates where the other half of the conflict occurred.

If the annotations on a function mention the IRQL and do not explicitly apply \_IRQL\_requires\_max\_, the Code Analysis tool implicitly applies the annotation \_IRQL\_requires\_max\_(DISPATCH\_LEVEL), which is typically correct with rare exceptions. Implicitly applying this as the default eliminates a lot of annotation clutter and makes the exceptions much more visible.

The \_IRQL\_requires\_min\_(PASSIVE\_LEVEL) annotation is always implied because the IRQL can go no lower; consequently, there is no corresponding explicit rule about minimum IRQL. Very few functions have both an upper bound other than DISPATCH\_LEVEL and a lower bound other than PASSIVE\_LEVEL.

Some functions are called in a context in which the called function cannot safely raise the IRQL above some maximum or, more often, cannot safely lower it below some minimum. The \_IRQL\_always\_function\_max\_ and \_IRQL\_always\_function\_min\_ annotations help PREfast find cases where this occurs unintentionally.

For example, functions of type DRIVER\_STARTIO are annotated with \_IRQL\_always\_function\_min\_(DISPATCH\_LEVEL). This means that during the execution of a DRIVER\_STARTIO function, it is an error to lower the IRQL below DISPATCH\_LEVEL. Other annotations indicate that the function must be entered and exited at DISPATCH\_LEVEL.

### <span id="Specifying_an_Explicit_IRQL"></span><span id="specifying_an_explicit_irql"></span><span id="SPECIFYING_AN_EXPLICIT_IRQL"></span>Specifying an Explicit IRQL

Use the \_IRQL\_raises\_ or \_IRQL\_requires\_ annotation to help PREfast better report an inconsistency that is discovered with \_IRQL\_requires\_max\_ or \_IRQL\_requires\_min\_ annotations because it then knows the IRQL.

The \_IRQL\_raises\_ annotation indicates that a function returns with the IRQL set to a new value. When you use the \_IRQL\_raises\_ annotation, it also effectively sets the \_drv\_maxFunctionIRQL annotation to the same IRQL value. However, if the function raises the IRQL higher than the final value and then lowers it to the final value, you should add an explicit \_IRQL\_always\_function\_max\_ annotation following the \_IRQL\_raises\_ annotation to allow for the higher IRQL value.

### <span id="Raising_or_Lowering_IRQL"></span><span id="raising_or_lowering_irql"></span><span id="RAISING_OR_LOWERING_IRQL"></span>Raising or Lowering IRQL

The \_IRQL\_raises\_ annotation indicates that the function must be used only to raise IRQL and must not be used to lower IRQL, even if the syntax of the function would allow it. KeRaiseIrql is an example of a function that should not be used to lower IRQL.

### <span id="Saving_and_Restoring_IRQL"></span><span id="saving_and_restoring_irql"></span><span id="SAVING_AND_RESTORING_IRQL"></span>Saving and Restoring IRQL

Use the \_IRQL\_saves\_ and \_IRQL\_restores\_ annotations to indicate that the current IRQL (whether it is known exactly or only approximately) is saved to or restored from the annotated parameter.

Some functions save and restore the IRQL implicitly. For example, the ExAcquireFastMutex system function saves the IRQL in an opaque location that is associated with the fast mutex object that the first parameter identifies; the saved IRQL is restored by the corresponding ExReleaseFastMutex function for that fast mutex object. To indicate these actions explicitly, use the \_IRQL\_saves\_global\_ and \_IRQL\_restores\_global\_ annotations. The *kind* and *param* parameters indicate where the IRQL value is saved. The location where the value is saved does not have to be precisely specified, as long as the annotations that save and restore the value are consistent.

### <span id="Maintaining_the_Same_IRQL"></span><span id="maintaining_the_same_irql"></span><span id="MAINTAINING_THE_SAME_IRQL"></span>Maintaining the Same IRQL

You should annotate any functions that your driver creates that change the IRQL using either the \_IRQL\_requires\_same\_ annotation or one of the other IRQL annotations to indicate that the change in IRQL is expected. In the absence of annotations that indicate any change in IRQL, the code analysis tools will issue a warning for any function that does not exit at the same IRQL at which the function was entered. If the change in IRQL is intended, add the appropriate annotation to suppress the error. If the change in IRQL is not intended, the code should be corrected.

### <span id="Saving_and_Restoring_IRQL_for_I_O_Cancellation_Routines"></span><span id="saving_and_restoring_irql_for_i_o_cancellation_routines"></span><span id="SAVING_AND_RESTORING_IRQL_FOR_I_O_CANCELLATION_ROUTINES"></span>Saving and Restoring IRQL for I/O Cancellation Routines

Use the \_IRQL\_uses\_cancel\_ annotation to indicate that the annotated parameter is the IRQL value that should be restored by a DRIVER\_CANCEL callback function. This annotation indicates that the function is a utility that is called from cancel routines and that it completes the requirements that were made on DRIVER\_CANCEL functions (that is, it discharges the obligation for the caller).

For example, the following is the declaration for the DRIVER\_CANCEL callback function type. One of the parameters is the IRQL that should be restored by this function. The annotations indicate all of the requirements of a cancel function.

```ManagedCPlusPlus
// Define driver cancel routine type.  //    
__drv_functionClass(DRIVER_CANCEL)  
_Requires_lock_held_(_Global_cancel_spin_lock_)  
_Releases_lock_(_Global_cancel_spin_lock_)  
_IRQL_requires_min_(DISPATCH_LEVEL)  
_IRQL_requires_(DISPATCH_LEVEL)  
typedef  
VOID  
DRIVER_CANCEL (  
    _Inout_ struct _DEVICE_OBJECT *DeviceObject,  
    _Inout_ _IRQL_uses_cancel_ struct _IRP *Irp  
    );  
  
typedef DRIVER_CANCEL *PDRIVER_CANCEL;  
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Drivers](sal-2-annotations-for-windows-drivers.md)

 

 






