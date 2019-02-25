---
title: Code Analysis for Drivers Warnings
description: Code Analysis for Drivers Warnings
ms.assetid: 61dba158-7e1b-42ee-9882-0ba9cef77b3c
keywords:
- PREfast for Drivers WDK , warnings
- warnings WDK PREfast for Drivers
- errors WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code Analysis for Drivers Warnings


This section lists and describes the warnings that the Code Analysis for Drivers reports when it detects a possible error in driver code. Note that some warnings are intended for kernel-mode code and can be ignored when analyzing user-mode drivers.

Code Analysis for Drivers reports the following types of warnings:

-   **General Warnings** (6000-6999): Potential errors in C and C++ syntax and general coding practice. For a description of these warnings, see [Code Analysis for C/C++ Warnings](/visualstudio/code-quality/code-analysis-for-c-cpp-warnings).

-   **Windows Specific Warnings** (28600-28799): These warnings are specific to certain patterns of use in Windows, but are not specific to drivers.

-   **Driver-Specific Warnings** (28100-28199): Errors in a driver's interaction with the application, with other drivers, and with the operating system.

-   **Annotation Errors** (28200-28299 and 36000-36999): These warnings indicate that an annotation has been incorrectly coded or used in an improper context. In most cases, the presence of such a warning indicates that the annotation is not having the desired (or any) effect.

-   **Memory Allocation Warnings** (30029-30035): These are memory allocation warnings.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="28101-wrong-function-type.md" data-raw-source="[C28101](28101-wrong-function-type.md)">C28101</a></p></td>
<td align="left"><p>warning C28101: The Drivers module has inferred that the current function is not the correct type of function</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28110-floating-point-hardware-protect.md" data-raw-source="[C28110](28110-floating-point-hardware-protect.md)">C28110</a></p></td>
<td align="left"><p>warning C28110: Drivers must protect floating-point hardware state. See use of float</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28111-floating-point-irql-mismatch.md" data-raw-source="[C28111](28111-floating-point-irql-mismatch.md)">C28111</a></p></td>
<td align="left"><p>warning C28111: The IRQL where the floating-point state was saved does not match the current IRQL (for this restore operation).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28114-improper-irp-stack-copy.md" data-raw-source="[C28114](28114-improper-irp-stack-copy.md)">C28114</a></p></td>
<td align="left"><p>warning: C28114: Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28120-irql-execution-too-low.md" data-raw-source="[C28120](28120-irql-execution-too-low.md)">C28120</a></p></td>
<td align="left"><p>warning C28120: The function is not permitted to be called at the current IRQ level. The current level is too low.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28121-irq-execution-too-high.md" data-raw-source="[C28121](28121-irq-execution-too-high.md)">C28121</a></p></td>
<td align="left"><p>warning C28121: The function is not permitted to be called at the current IRQ level. The current level is too high.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28122-inconsistent-irq-level-calls-low.md" data-raw-source="[C28122](28122-inconsistent-irq-level-calls-low.md)">C28122</a></p></td>
<td align="left"><p>warning C28122: The function is not permitted to be called at a low IRQ level. Prior function calls are inconsistent with this constraint.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28123-inconsistent-irq-level-calls-high.md" data-raw-source="[C28123](28123-inconsistent-irq-level-calls-high.md)">C28123</a></p></td>
<td align="left"><p>warning C28123: The function is not permitted to be called at a high IRQ level. Prior function calls are inconsistent with this constraint.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28124-call-below-minimum-irq-level.md" data-raw-source="[C28124](28124-call-below-minimum-irq-level.md)">C28124</a></p></td>
<td align="left"><p>warning C28124: The call to causes the IRQ Level to be set below the minimum acceptable for the function being analyzed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28126-accessmode-param-incorrect.md" data-raw-source="[C28126](28126-accessmode-param-incorrect.md)">C28126</a></p></td>
<td align="left"><p>warning C28126: The AccessMode parameter to ObReferenceObject* should be IRP-&gt;RequestorMode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28127-function-routine-mismatch.md" data-raw-source="[C28127](28127-function-routine-mismatch.md)">C28127</a></p></td>
<td align="left"><p>warning C28127: The function being used as a routine does not exactly match the type expected.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28128-structure-member-directly-accessed.md" data-raw-source="[C28128](28128-structure-member-directly-accessed.md)">C28128</a></p></td>
<td align="left"><p>warning C28128: An access to a field has been made directly. It should be made by a routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28129-assignment-made-to-operand.md" data-raw-source="[C28129](28129-assignment-made-to-operand.md)">C28129</a></p></td>
<td align="left"><p>warning C28129: An assignment has been made to an operand, which should only be modified using bit sets and clears</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28131-driverentry-saving-pointer-to-buffer.md" data-raw-source="[C28131](28131-driverentry-saving-pointer-to-buffer.md)">C28131</a></p></td>
<td align="left"><p>warning C28131: The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28132-driver-taking-the-size-of-pointer.md" data-raw-source="[C28132](28132-driver-taking-the-size-of-pointer.md)">C28132</a></p></td>
<td align="left"><p>warning C28132: Taking the size of pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28133-ioinitializetimer-is-best-called-from-add-device.md" data-raw-source="[C28133](28133-ioinitializetimer-is-best-called-from-add-device.md)">C28133</a></p></td>
<td align="left"><p>warning C28133: IoInitializeTimer is best called from AddDevice</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28134-pool-tag-type-should-be-integral.md" data-raw-source="[C28134](28134-pool-tag-type-should-be-integral.md)">C28134</a></p></td>
<td align="left"><p>warning C28134: The type of a pool tag should be integral, not a string or string pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28135-first-argument-to-kewaitforsingleobject.md" data-raw-source="[C28135](28135-first-argument-to-kewaitforsingleobject.md)">C28135</a></p></td>
<td align="left"><p>warning C28135: If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28139-argument-operand-should-exactly-match.md" data-raw-source="[C28139](28139-argument-operand-should-exactly-match.md)">C28139</a></p></td>
<td align="left"><p>warning C28139: The argument should exactly match the type</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28141-argument-lowers-irq-level.md" data-raw-source="[C28141](28141-argument-lowers-irq-level.md)">C28141</a></p></td>
<td align="left"><p>warning C28141: The argument causes the IRQ Level to be set below the current IRQL, and this function cannot be used for that purpose</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28143-iomarkirppending-must-return-statuspending.md" data-raw-source="[C28143](28143-iomarkirppending-must-return-statuspending.md)">C28143</a></p></td>
<td align="left"><p>warning C28143: A dispatch routine that calls IoMarkIrpPending must also return STATUS_PENDING</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28144-cancelirql-should-be-current-irql.md" data-raw-source="[C28144](28144-cancelirql-should-be-current-irql.md)">C28144</a></p></td>
<td align="left"><p>warning C28144: Within a cancel routine, at the point of exit, the IRQL in Irp-&gt;CancelIrql should be the current IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28145-opaque-mdl-structure-should-not-be-modified.md" data-raw-source="[C28145](28145-opaque-mdl-structure-should-not-be-modified.md)">C28145</a></p></td>
<td align="left"><p>warning C28145: The opaque MDL structure should not be modified by a driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28146-kernel-mode-drivers-should-use-ntstrsafe.md" data-raw-source="[C28146](28146-kernel-mode-drivers-should-use-ntstrsafe.md)">C28146</a></p></td>
<td align="left"><p>warning C28146: Kernel Mode drivers should use ntstrsafe.h, not strsafe.h. Found in source file</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28147-improper-use-of-default-pool-tag.md" data-raw-source="[C28147](28147-improper-use-of-default-pool-tag.md)">C28147</a></p></td>
<td align="left"><p>warning C28147: The use of a default pool tag (&#39; kdD&#39; or &#39; mdW&#39;) for calls to this function defeats the purpose of pool tagging</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28150-function-causes-irq-level-to-be-set-above-max.md" data-raw-source="[C28150](28150-function-causes-irq-level-to-be-set-above-max.md)">C28150</a></p></td>
<td align="left"><p>warning C28150: The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28151-illegal-irql-value.md" data-raw-source="[C28151](28151-illegal-irql-value.md)">C28151</a></p></td>
<td align="left"><p>warning C28151: The value is not a legal value for an IRQL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28152-do-device-initializing-flag-not-cleared.md" data-raw-source="[C28152](28152-do-device-initializing-flag-not-cleared.md)">C28152</a></p></td>
<td align="left"><p>warning C28152: The return from an AddDevice-like function unexpectedly DO_DEVICE_INITIALIZING</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28153-irql-annotation-eval-context.md" data-raw-source="[C28153](28153-irql-annotation-eval-context.md)">C28153</a></p></td>
<td align="left"><p>warning C28153: The value for an IRQL from annotation could not be evaluated in this context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28156-irql-inconsistent-with-required-irq-value.md" data-raw-source="[C28156](28156-irql-inconsistent-with-required-irq-value.md)">C28156</a></p></td>
<td align="left"><p>warning C28156: The actual IRQL is inconsistent with the required IRQL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28157-function-irql-never-restored.md" data-raw-source="[C28157](28157-function-irql-never-restored.md)">C28157</a></p></td>
<td align="left"><p>warning C28157: The IRQL was never restored</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28158-no-irql-was-saved.md" data-raw-source="[C28158](28158-no-irql-was-saved.md)">C28158</a></p></td>
<td align="left"><p>warning C28158: No IRQL was saved</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28161-exiting-without-right-to-use-floating-hardware.md" data-raw-source="[C28161](28161-exiting-without-right-to-use-floating-hardware.md)">C28161</a></p></td>
<td align="left"><p>warning C28161: Exiting without acquiring the right to use floating hardware</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28162-exiting-while-holding-right-to-use-floating-hardware.md" data-raw-source="[C28162](28162-exiting-while-holding-right-to-use-floating-hardware.md)">C28162</a></p></td>
<td align="left"><p>warning C28162: Exiting while holding the right to use floating-point hardware</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28165-class-function-pointer-mismatch.md" data-raw-source="[C28165](28165-class-function-pointer-mismatch.md)">C28165</a></p></td>
<td align="left"><p>warning C28165: The function pointer of class does not match the function class</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28166-function-does-not-restore-irql-value.md" data-raw-source="[C28166](28166-function-does-not-restore-irql-value.md)">C28166</a></p></td>
<td align="left"><p>warning C28166: The function does not restore the IRQL to the value that was current at function entry and is required to do so.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28167-function-changes-irql-without-restore.md" data-raw-source="[C28167](28167-function-changes-irql-without-restore.md)">C28167</a></p></td>
<td align="left"><p>warning C28167: The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28168-dispatch-function-dispatch-annotation.md" data-raw-source="[C28168](28168-dispatch-function-dispatch-annotation.md)">C28168</a></p></td>
<td align="left"><p>warning C28168: The dispatch function does not have a <strong><em>Dispatch_type</em></strong> annotation matching this dispatch table entry</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28169-dispatch-function-does-not-have-proper-annotation.md" data-raw-source="[C28169](28169-dispatch-function-does-not-have-proper-annotation.md)">C28169</a></p></td>
<td align="left"><p>warning C28169: The dispatch function does not have any <strong><em>Dispatch_type</em></strong> annotations</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28170-pageable-code-macro-not-found.md" data-raw-source="[C28170](28170-pageable-code-macro-not-found.md)">C28170</a></p></td>
<td align="left"><p>warning C28170: The function has been declared to be in a paged segment, but neither PAGED_CODE nor PAGED_CODE_LOCKED was found</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28171-function-has-more-than-one-page-macro-instance.md" data-raw-source="[C28171](28171-function-has-more-than-one-page-macro-instance.md)">C28171</a></p></td>
<td align="left"><p>warning C28171: The function has more than one instance of PAGED_CODE or PAGED_CODE_LOCKED</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28172-function-macros-not-in-paged-segment.md" data-raw-source="[C28172](28172-function-macros-not-in-paged-segment.md)">C28172</a></p></td>
<td align="left"><p>warning C28172: The function has PAGED_CODE or PAGED_CODE_LOCKED but is not declared to be in a paged segment</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28173-function-incorrectly-adapts-to-memory-above-4gb.md" data-raw-source="[C28173](28173-function-incorrectly-adapts-to-memory-above-4gb.md)">C28173</a></p></td>
<td align="left"><p>warning C28173: The current function appears to incorrectly adapt to physical memory above 4 GB</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28175struct-member-should-not-be-accessed-by-driver.md" data-raw-source="[C28175](28175struct-member-should-not-be-accessed-by-driver.md)">C28175</a></p></td>
<td align="left"><p>warning C28175: The member of struct should not be accessed by a driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28176-struct-member-should-not-be-modified-by-driver.md" data-raw-source="[C28176](28176-struct-member-should-not-be-modified-by-driver.md)">C28176</a></p></td>
<td align="left"><p>warning C28176: The member of struct should not be modified by a driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28177-function-annotated-with-more-than-one-class.md" data-raw-source="[C28177](28177-function-annotated-with-more-than-one-class.md)">C28177</a></p></td>
<td align="left"><p>warning C28177: Function is annotated with more than one function class. All but one will be ignored.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28260-syntax-error-in-function-property.md" data-raw-source="[C28260](28260-syntax-error-in-function-property.md)">C28260</a></p></td>
<td align="left"><p>warning C28260: A syntax error in the annotations was found while parsing for a property inside a function</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28266-function-property-syntax-error.md" data-raw-source="[C28266](28266-function-property-syntax-error.md)">C28266</a></p></td>
<td align="left"><p>A syntax error in the annotations was found for the property in the function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28268-function-class-does-not-match-typedef.md" data-raw-source="[C28268](28268-function-class-does-not-match-typedef.md)">C28268</a></p></td>
<td align="left"><p>warning C28268: The function class on the function does not match the function class on the typedef used here</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28601-avoid-blocking-on-hwnd-broadcast.md" data-raw-source="[C28601](28601-avoid-blocking-on-hwnd-broadcast.md)">C28601</a></p></td>
<td align="left"><p>warning C28601: Avoid blocking on HWND_BROADCAST</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28602-avoid-calling-sendmessagetimeout-with-hwnd-broadcast.md" data-raw-source="[C28602](28602-avoid-calling-sendmessagetimeout-with-hwnd-broadcast.md)">C28602</a></p></td>
<td align="left"><p>warning C28602: Avoid calling SendMessageTimeout with HWND_BROADCAST</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28604-smto-abortifhung-with-0-timeout-.md" data-raw-source="[C28604](28604-smto-abortifhung-with-0-timeout-.md)">C28604</a></p></td>
<td align="left"><p>warning C28604: Avoid calling SendMessageTimeout with SMTO_ABORTIFHUNG with a timeout of 0</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28615-must-call-resetstkoflw-in-except-block.md" data-raw-source="[C28615](28615-must-call-resetstkoflw-in-except-block.md)">C28615</a></p></td>
<td align="left"><p>warning C28615: Must call _resetstkoflw in the __except() block when calling _alloca in the __try block. Don&#39;t call _resetstkoflw from inside a catch() block</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28616-multithreaded-av-condition.md" data-raw-source="[C28616](28616-multithreaded-av-condition.md)">C28616</a></p></td>
<td align="left"><p>warning C28616: Multithreaded AV condition</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28617-avoid-using-the-return-value-of-beginthread.md" data-raw-source="[C28617](28617-avoid-using-the-return-value-of-beginthread.md)">C28617</a></p></td>
<td align="left"><p>warning C28617: Avoid using the return value of _beginthread(). Use _beginthreadex() instead</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28623-unsigned-cast-of-getmessagepos-coordinates.md" data-raw-source="[C28623](28623-unsigned-cast-of-getmessagepos-coordinates.md)">C28623</a></p></td>
<td align="left"><p>warning C28623: Unsigned cast of GetMessagePos() coordinates. Use GET_X_LPARAM/GET_Y_LPARAM instead of LOWORD/HIWORD</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28624-no-release-call-to-match-incremented-refcount.md" data-raw-source="[C28624](28624-no-release-call-to-match-incremented-refcount.md)">C28624</a></p></td>
<td align="left"><p>warning C28624: No call to Release() to match incremented refcount from LResultFromObject</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28625-sensitive-data-may-be-retained.md" data-raw-source="[C28625](28625-sensitive-data-may-be-retained.md)">C28625</a></p></td>
<td align="left"><p>warning C28625: Function call used to clear sensitive data will be optimized away</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28636-calling-localfree-on-non-allocated-pointer.md" data-raw-source="[C28636](28636-calling-localfree-on-non-allocated-pointer.md)">C28636</a></p></td>
<td align="left"><p>warning C28636: Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28637-calling-function-in-a-global-initializer-is-unsafe.md" data-raw-source="[C28637](28637-calling-function-in-a-global-initializer-is-unsafe.md)">C28637</a></p></td>
<td align="left"><p>warning C28637: Calling the function in a global initializer is unsafe</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28638-function-delayload-stub-is-missing-declaration-.md" data-raw-source="[C28638](28638-function-delayload-stub-is-missing-declaration-.md)">C28638</a></p></td>
<td align="left"><p>warning C28638: function delayload stub is missing a matching declaration</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28639-calling-close-handle-with-string.md" data-raw-source="[C28639](28639-calling-close-handle-with-string.md)">C28639</a></p></td>
<td align="left"><p>warning C28639: Calling close handle with string</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28640-delayload-function-stub-should-be-a-static-function.md" data-raw-source="[C28640](28640-delayload-function-stub-should-be-a-static-function.md)">C28640</a></p></td>
<td align="left"><p>warning C28640: function delayload stub should be a static function</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28644-return-value-from-dpa-insertptr-not-checked.md" data-raw-source="[C28644](28644-return-value-from-dpa-insertptr-not-checked.md)">C28644</a></p></td>
<td align="left"><p>warning C28644: Return value from DPA_InsertPtr not checked</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28645-messagebox-called-using-the-question-mark-symbol.md" data-raw-source="[C28645](28645-messagebox-called-using-the-question-mark-symbol.md)">C28645</a></p></td>
<td align="left"><p>warning C28645: MessageBox was called using the question mark message symbol which is no longer recommended</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28648-pulseevent-is-an-unreliable-function.md" data-raw-source="[C28648](28648-pulseevent-is-an-unreliable-function.md)">C28648</a></p></td>
<td align="left"><p>warning C28648: PulseEvent is an unreliable function</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28649-automatic-or-global-stack-arrays-are-never-null.md" data-raw-source="[C28649](28649-automatic-or-global-stack-arrays-are-never-null.md)">C28649</a></p></td>
<td align="left"><p>warning C28649: Automatic or Global Stack Arrays are never NULL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28650-generic-value-is-not-treated-as-failure.md" data-raw-source="[C28650](28650-generic-value-is-not-treated-as-failure.md)">C28650</a></p></td>
<td align="left"><p>warning C28650: The type for which !0 is being used does not treat it as failure case.</p>
<p>Returning a status value such as !TRUE is not the same as returning a status value that indicates failure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28651-member-function-pointers-cause-write-pages-copy.md" data-raw-source="[C28651](28651-member-function-pointers-cause-write-pages-copy.md)">C28651</a></p></td>
<td align="left"><p>warning C28651: Static initializer causes copy on write pages due to member function pointers</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28652-overloaded-bitwise-operators-cause-write-pages-copy.md" data-raw-source="[C28652](28652-overloaded-bitwise-operators-cause-write-pages-copy.md)">C28652</a></p></td>
<td align="left"><p>warning C28652: Static initializer causes copy on write pages due to overloaded bitwise operators</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28714-ntstatus-cast-between-semantically-different-integer-types.md" data-raw-source="[C28714](28714-ntstatus-cast-between-semantically-different-integer-types.md)">C28714</a></p></td>
<td align="left"><p>warning C28714: Cast between semantically different integer types</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28715-boolean-cast-between-semantically-different-integer-types.md" data-raw-source="[C28715](28715-boolean-cast-between-semantically-different-integer-types.md)">C28715</a></p></td>
<td align="left"><p>warning C28715: Cast between semantically different integer types</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28716-compiler-inserted-cast-between-semantically-different-integral.md" data-raw-source="[C28716](28716-compiler-inserted-cast-between-semantically-different-integral.md)">C28716</a></p></td>
<td align="left"><p>warning C28716: Compiler-inserted cast between semantically different integral types</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28717-invalid-variant-type.md" data-raw-source="[C28717](28717-invalid-variant-type.md)">C28717</a></p></td>
<td align="left"><p>warning C28717: Invalid VARIANT type</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28718-unannotated-buffer.md" data-raw-source="[C28718](28718-unannotated-buffer.md)">C28718</a></p></td>
<td align="left"><p>warning C28718: Unannotated buffer</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28719-banned-api-usage-use-updated-function-replacement.md" data-raw-source="[C28719](28719-banned-api-usage-use-updated-function-replacement.md)">C28719</a></p></td>
<td align="left"><p>warning C28719: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28720-banned-api-usage-use-updated-function-replacement.md" data-raw-source="[C28720](28720-banned-api-usage-use-updated-function-replacement.md)">C28720</a></p></td>
<td align="left"><p>warning C28720: Banned API Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28721-deprecated-performance-counter-architecture.md" data-raw-source="[C28721](28721-deprecated-performance-counter-architecture.md)">C28721</a></p></td>
<td align="left"><p>warning C28721: Deprecated performance counter architecture</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28722-unannotated-function-declaration-buffer.md" data-raw-source="[C28722](28722-unannotated-function-declaration-buffer.md)">C28722</a></p></td>
<td align="left"><p>warning C28722: Unannotated buffer in function declaration</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28723-unannotated-buffer-without-declaration.md" data-raw-source="[C28723](28723-unannotated-buffer-without-declaration.md)">C28723</a></p></td>
<td align="left"><p>warning C28723: Unannotated buffer in function definition that has no corresponding declaration</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28725-use-watson-instead.md" data-raw-source="[C28725](28725-use-watson-instead.md)">C28725</a></p></td>
<td align="left"><p>warning C28725: Use Watson instead of this SetUnhandledExceptionFilter</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28726-banned-api-usage-use-updated-function-replacement.md" data-raw-source="[C28726](28726-banned-api-usage-use-updated-function-replacement.md)">C28726</a></p></td>
<td align="left"><p>warning C28726: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28727-banned-api-usage-use-updated-function-replacement.md" data-raw-source="[C28727](28727-banned-api-usage-use-updated-function-replacement.md)">C28727</a></p></td>
<td align="left"><p>warning C28727: Banned API Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28728-banned-api-usage-use-updated-function-replacement.md" data-raw-source="[C28728](28728-banned-api-usage-use-updated-function-replacement.md)">C28728</a></p></td>
<td align="left"><p>warning C28728: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28730-possible-null-character-assignment.md" data-raw-source="[C28730](28730-possible-null-character-assignment.md)">C28730</a></p></td>
<td align="left"><p>warning C28730: Possible assignment of &#39;\0&#39; directly to a pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28735-banned-crimson-api-usage.md" data-raw-source="[C28735](28735-banned-crimson-api-usage.md)">C28735</a></p></td>
<td align="left"><p>warning C28735: Banned Crimson API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28736-legacy-crimson-or-perflib-banned-argument-used.md" data-raw-source="[C28736](28736-legacy-crimson-or-perflib-banned-argument-used.md)">C28736</a></p></td>
<td align="left"><p>warning C28736: Banned API Argument Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28740-unannotated-unsigned-buffer.md" data-raw-source="[C28740](28740-unannotated-unsigned-buffer.md)">C28740</a></p></td>
<td align="left"><p>warning C28740: Unannotated unsigned buffer</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28741-unannotated-non-constant-string-buffer-in-function.md" data-raw-source="[C28741](28741-unannotated-non-constant-string-buffer-in-function.md)">C28741</a></p></td>
<td align="left"><p>warning C28741: Unannotated buffer in the function</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28742-unnanotated-non-constant-buffer-in-function.md" data-raw-source="[C28742](28742-unnanotated-non-constant-buffer-in-function.md)">C28742</a></p></td>
<td align="left"><p>warning C28742: Unannotated buffer in the function</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28750-banned-istrlen-usage.md" data-raw-source="[C28750](28750-banned-istrlen-usage.md)">C28750</a></p></td>
<td align="left"><p>warning C28750: Banned usage of lstrlen and its variants</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28751-banned-exallocatepool-usage.md" data-raw-source="[C28751](28751-banned-exallocatepool-usage.md)">C28751</a></p></td>
<td align="left"><p>warning C28751: Banned usage of ExAllocatePool and its variants</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="28752-banned-kernel32-advapi32-usage.md" data-raw-source="[C28752](28752-banned-kernel32-advapi32-usage.md)">C28752</a></p></td>
<td align="left"><p>warning C28752: Banned usage of kernel32 or advapi32 API</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="28753-relying-on-undefined-order-of-evalutation-params.md" data-raw-source="[C28753](28753-relying-on-undefined-order-of-evalutation-params.md)">C28753</a></p></td>
<td align="left"><p>warning C28753: Relying on undefined order of evaluation of parameters</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="30029-memory-allocating-function-requests-executable-memory.md" data-raw-source="[C30029](30029-memory-allocating-function-requests-executable-memory.md)">C30029</a></p></td>
<td align="left"><p>warning C30029: Calling a memory allocating function that requests executable memory</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="30030-parameter-indicates-executable-memory.md" data-raw-source="[C30030](30030-parameter-indicates-executable-memory.md)">C30030</a></p></td>
<td align="left"><p>warning C30030: Calling a memory allocating function and passing a parameter that indicates executable memory</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="30031-pool-n-optin-called-before-entry-function.md" data-raw-source="[C30031](30031-pool-n-optin-called-before-entry-function.md)">C30031</a></p></td>
<td align="left"><p>warning C30031: Calling a memory allocating function and passing a parameter that indicates executable memory</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="30032-forcing-request-of-executable-memory.md" data-raw-source="[C30032](30032-forcing-request-of-executable-memory.md)">C30032</a></p></td>
<td align="left"><p>warning C30032: Calling a memory allocating function and forcing the request of executable memory through use of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh920401" data-raw-source="[POOL_NX_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401)">POOL_NX_OPTOUT</a> directive</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="30033-executable-allocation-detected-with-pool-nx-optin.md" data-raw-source="[C30033](30033-executable-allocation-detected-with-pool-nx-optin.md)">C30033</a></p></td>
<td align="left"><p>warning C30033: Executable allocation was detected in a driver compiled with <a href="https://msdn.microsoft.com/library/windows/hardware/hh920402" data-raw-source="[POOL_NX_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402)">POOL_NX_OPTIN</a>. This driver has been determined to be loaded at run time by another driver. Please verify that the loading driver calls <strong>ExInitializeDriverRuntime(<em>DrvRtPoolNxOptIn</em>)</strong> in its DriverEntry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="30034-passing-flag-value-to-allocating-function.md" data-raw-source="[C30034](30034-passing-flag-value-to-allocating-function.md)">C30034</a></p></td>
<td align="left"><p>warning C30034: Passing a flag value to an allocating function that could result in executable memory being allocated. Please verify that the allocating function is not requesting a form of executable nonpaged pool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="30035-function-call-must-be-made-inside-init-function.md" data-raw-source="[C30035](30035-function-call-must-be-made-inside-init-function.md)">C30035</a></p></td>
<td align="left"><p>warning C30035: A call was made to a function that must be made from inside the initialization function (for example, <strong>DriverEntry()</strong> or <strong>DllInitialize()</strong>). PREfast was unable to determine if the call was made from the initialization function.</p></td>
</tr>
</tbody>
</table>

 

 

 

