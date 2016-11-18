---
title: Code Analysis for Drivers Warnings
description: Code Analysis for Drivers Warnings
ms.assetid: 61dba158-7e1b-42ee-9882-0ba9cef77b3c
keywords: ["PREfast for Drivers WDK , warnings", "warnings WDK PREfast for Drivers", "errors WDK PREfast for Drivers"]
---

# Code Analysis for Drivers Warnings


This section lists and describes the warnings that the Code Analysis for Drivers reports when it detects a possible error in driver code. Note that some warnings are intended for kernel-mode code and can be ignored when analyzing user-mode drivers.

Code Analysis for Drivers reports the following types of warnings:

-   **General Warnings** (6000-6999): Potential errors in C and C++ syntax and general coding practice. For a description of these warnings, see [Code Analysis for C/C++ Warnings](http://go.microsoft.com/fwlink/p/?linkid=232389).

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
<td align="left"><p>[C28101](28101---the-drivers-module-has-inferred-that-the-current-function-is-a.md)</p></td>
<td align="left"><p>warning C28101: The Drivers module has inferred that the current function is not the correct type of function</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28110](28110---drivers-must-protect-floating-point-hardware-state--see-use-of.md)</p></td>
<td align="left"><p>warning C28110: Drivers must protect floating-point hardware state. See use of float</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28111](28111---the-irql-where-the-floating-point-state-was-saved-does-not-mat.md)</p></td>
<td align="left"><p>warning C28111: The IRQL where the floating-point state was saved does not match the current IRQL (for this restore operation).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28114](28114---copying-a-whole-irp-leaves-certain-fields-initialized-that-sho.md)</p></td>
<td align="left"><p>warning: C28114: Copying a whole IRP stack entry leaves certain fields initialized that should be cleared or updated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28120](28120---the-function--function--is-not-permitted-to-be-called-at-the-c.md)</p></td>
<td align="left"><p>warning C28120: The function is not permitted to be called at the current IRQ level. The current level is too low.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28121](28121---the-function--function--is-not-permitted-to-be-called-at-the-c.md)</p></td>
<td align="left"><p>warning C28121: The function is not permitted to be called at the current IRQ level. The current level is too high.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28122](28122---the-function--function--is-not-permitted-to-be-called-at-a-low.md)</p></td>
<td align="left"><p>warning C28122: The function is not permitted to be called at a low IRQ level. Prior function calls are inconsistent with this constraint.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28123](28123---the-function--function--is-not-permitted-to-be-called-at-a-hig.md)</p></td>
<td align="left"><p>warning C28123: The function is not permitted to be called at a high IRQ level. Prior function calls are inconsistent with this constraint.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28124](28124---the-call-to--function--causes-the-irq-level-to-be-set-below-th.md)</p></td>
<td align="left"><p>warning C28124: The call to causes the IRQ Level to be set below the minimum acceptable for the function being analyzed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28126](28126---the-accessmode-parameter-to-obreferenceobject--should-be-irp--.md)</p></td>
<td align="left"><p>warning C28126: The AccessMode parameter to ObReferenceObject* should be IRP-&gt;RequestorMode</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28127](28127---the-function-being-used-as-a--function--routine-does-not-exact.md)</p></td>
<td align="left"><p>warning C28127: The function being used as a routine does not exactly match the type expected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28128](28128---an-access-to--field--has-been-made-directly--it-should-be-made.md)</p></td>
<td align="left"><p>warning C28128: An access to a field has been made directly. It should be made by a routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28129](28129---an-assignment-has-been-made-to--operand--which-should-only-be-.md)</p></td>
<td align="left"><p>warning C28129: An assignment has been made to an operand, which should only be modified using bit sets and clears</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28131](28131---the-driverentry-routine-should-save-a-copy-of-the-argument--ar.md)</p></td>
<td align="left"><p>warning C28131: The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28132](28132---taking-the-size-of-pointer--operand-.md)</p></td>
<td align="left"><p>warning C28132: Taking the size of pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28133](28133---ioinitializetimer-is-best-called-from-adddevice.md)</p></td>
<td align="left"><p>warning C28133: IoInitializeTimer is best called from AddDevice</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28134](28134---the-type-of-a-pool-tag-should-be-integral--not-a-string-or-str.md)</p></td>
<td align="left"><p>warning C28134: The type of a pool tag should be integral, not a string or string pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28135](28135---if-the-first-argument-to-kewaitforsingleobject-is-a-local-vari.md)</p></td>
<td align="left"><p>warning C28135: If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28139](28139---the-argument--operand--should-exactly-match-the-type--typename.md)</p></td>
<td align="left"><p>warning C28139: The argument should exactly match the type</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28141](28141---the-argument--expression--causes-the-irq-level-to-be-set-below.md)</p></td>
<td align="left"><p>warning C28141: The argument causes the IRQ Level to be set below the current IRQL, and this function cannot be used for that purpose</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28143](28143---a-dispatch-routine-that-calls-iomarkirppending-must-also-retur.md)</p></td>
<td align="left"><p>warning C28143: A dispatch routine that calls IoMarkIrpPending must also return STATUS_PENDING</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28144](28144---within-a-cancel-routine--at-the-point-of-exit--the-irql-in-irp.md)</p></td>
<td align="left"><p>warning C28144: Within a cancel routine, at the point of exit, the IRQL in Irp-&gt;CancelIrql should be the current IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28145](28145---the-opaque-mdl-structure-should-not-be-modified-by-a-driver.md)</p></td>
<td align="left"><p>warning C28145: The opaque MDL structure should not be modified by a driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28146](28146---kernel-mode-drivers-should-use-ntstrsafe-h--not-strsafe-h.md)</p></td>
<td align="left"><p>warning C28146: Kernel Mode drivers should use ntstrsafe.h, not strsafe.h. Found in source file</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28147](28147---the-use-of-a-default-pool-tag----kdd--or---mdw---for-calls-to-.md)</p></td>
<td align="left"><p>warning C28147: The use of a default pool tag (' kdD' or ' mdW') for calls to this function defeats the purpose of pool tagging</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28150](28150---the-function--function--causes-the-irq-level-to-be-set-above-t.md)</p></td>
<td align="left"><p>warning C28150: The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28151](28151---the-value-of--irql--is-not-a-legal-value-for-an-irql.md)</p></td>
<td align="left"><p>warning C28151: The value is not a legal value for an IRQL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28152](28152---the-return-from-an-adddevice-like-function-unexpectedly--clear.md)</p></td>
<td align="left"><p>warning C28152: The return from an AddDevice-like function unexpectedly DO_DEVICE_INITIALIZING</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28153](28153---the-value-for-an-irql-from-annotation--type--could-not-be-eval.md)</p></td>
<td align="left"><p>warning C28153: The value for an IRQL from annotation could not be evaluated in this context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28156](28156---the-actual-irql--actual--is-inconsistent-with-the-required-irq.md)</p></td>
<td align="left"><p>warning C28156: The actual IRQL is inconsistent with the required IRQL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28157](28157---the-irql-in--function--was-never-restored.md)</p></td>
<td align="left"><p>warning C28157: The IRQL was never restored</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28158](28158---no-irql-was-saved-into--variable-.md)</p></td>
<td align="left"><p>warning C28158: No IRQL was saved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28161](28161---exiting-without-acquiring-the-right-to-use-floating-hardware.md)</p></td>
<td align="left"><p>warning C28161: Exiting without acquiring the right to use floating hardware</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28162](28162---exiting-while-holding-the-right-to-use-floating-point-hardware.md)</p></td>
<td align="left"><p>warning C28162: Exiting while holding the right to use floating-point hardware</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28165](28165---the-function-pointer-of-class--class1--does-not-match-the-func.md)</p></td>
<td align="left"><p>warning C28165: The function pointer of class does not match the function class</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28166](28166---this-function--function--does-not-restore-the-irql-to-the-valu.md)</p></td>
<td align="left"><p>warning C28166: The function does not restore the IRQL to the value that was current at function entry and is required to do so.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28167](28167---this-function--function--changes-the-irql-and-does-not-restore.md)</p></td>
<td align="left"><p>warning C28167: The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28168](28168---the-dispatch-function--function--does-not-have-a---drv-dispatc.md)</p></td>
<td align="left"><p>warning C28168: The dispatch function does not have a <strong>_Dispatch_type_</strong> annotation matching this dispatch table entry</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28169](28169---the-dispatch-function--function--does-not-have-any---drv-dispa.md)</p></td>
<td align="left"><p>warning C28169: The dispatch function does not have any <strong>_Dispatch_type_</strong> annotations</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28170](28170---the-current-function--function--has-been-declared-to-be-in-a-p.md)</p></td>
<td align="left"><p>warning C28170: The function has been declared to be in a paged segment, but neither PAGED_CODE nor PAGED_CODE_LOCKED was found</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28171](28171---the-current-function--function--has-more-than-one-instance-of-.md)</p></td>
<td align="left"><p>warning C28171: The function has more than one instance of PAGED_CODE or PAGED_CODE_LOCKED</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28172](28172---the-current-function--function--has-paged-code-or-paged-code-l.md)</p></td>
<td align="left"><p>warning C28172: The function has PAGED_CODE or PAGED_CODE_LOCKED but is not declared to be in a paged segment</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28173](28173--the-current-function-appears-to-incorrectly-adapt-to-physical-m.md)</p></td>
<td align="left"><p>warning C28173: The current function appears to incorrectly adapt to physical memory above 4 GB</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28175](28175---the--member--member-of--struct--should-not-be-accessed-by-a-dr.md)</p></td>
<td align="left"><p>warning C28175: The member of struct should not be accessed by a driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28176](28176---the--member--member-of--struct--should-not-be-modified-by-a-dr.md)</p></td>
<td align="left"><p>warning C28176: The member of struct should not be modified by a driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28177](c28177.md)</p></td>
<td align="left"><p>warning C28177: Function is annotated with more than one function class. All but one will be ignored.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28260](28260---a-syntax-error-in-the-annotations-was-found-for-function--func.md)</p></td>
<td align="left"><p>warning C28260: A syntax error in the annotations was found while parsing for a property inside a function</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28266](28266--28267----a-syntax-error-in-the-annotations-was-found-for-functi.md)</p></td>
<td align="left"><p>A syntax error in the annotations was found for the property in the function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28268](28268---the-function-class--class--on-the-function-does-not-match-the-.md)</p></td>
<td align="left"><p>warning C28268: The function class on the function does not match the function class on the typedef used here</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28601](28601---avoid-blocking-on-hwnd-broadcast.md)</p></td>
<td align="left"><p>warning C28601: Avoid blocking on HWND_BROADCAST</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28602](28602---avoid-calling-sendmessagetimeout-with-hwnd-broadcast.md)</p></td>
<td align="left"><p>warning C28602: Avoid calling SendMessageTimeout with HWND_BROADCAST</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28604](28604---avoid-calling-sendmessagetimeout-with-smto-abortifhung-with-a-.md)</p></td>
<td align="left"><p>warning C28604: Avoid calling SendMessageTimeout with SMTO_ABORTIFHUNG with a timeout of 0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28615](28615---must-call-resetstkoflw-in-the-except---block-when-calling-allo.md)</p></td>
<td align="left"><p>warning C28615: Must call _resetstkoflw in the __except() block when calling _alloca in the __try block. Don't call _resetstkoflw from inside a catch() block</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28616](28616---multithreaded-av-condition--after-interlockeddecrement-this-m-.md)</p></td>
<td align="left"><p>warning C28616: Multithreaded AV condition</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28617](28617---avoid-using-the-return-value-of--beginthread-----use--beginthr.md)</p></td>
<td align="left"><p>warning C28617: Avoid using the return value of _beginthread(). Use _beginthreadex() instead</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28623](28623---unsigned-cast-of-getmessagepos---coordinates--use-get-x-lparam.md)</p></td>
<td align="left"><p>warning C28623: Unsigned cast of GetMessagePos() coordinates. Use GET_X_LPARAM/GET_Y_LPARAM instead of LOWORD/HIWORD</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28624](28624---no-call-to-release---to-match-incremented-refcount-from-lresul.md)</p></td>
<td align="left"><p>warning C28624: No call to Release() to match incremented refcount from LResultFromObject</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28625](28625---function-call-used-to-clear-sensitive-data-will-be-optimized-a.md)</p></td>
<td align="left"><p>warning C28625: Function call used to clear sensitive data will be optimized away</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28636](28636---calling-localfree-on-non-allocated-pointer-obtained-from-calls.md)</p></td>
<td align="left"><p>warning C28636: Calling LocalFree on non-allocated pointer obtained from calls to GetSecurityDescriptorOwner/Group/Dacl/Sacl</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28637](28637---calling--function--in-a-global-initializer-is-unsafe.md)</p></td>
<td align="left"><p>warning C28637: Calling the function in a global initializer is unsafe</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28638](28638-----function---delayload-stub-is-missing-a-matching-declaration-.md)</p></td>
<td align="left"><p>warning C28638: function delayload stub is missing a matching declaration</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28639](28639---calling-close-handle-with-string---string--.md)</p></td>
<td align="left"><p>warning C28639: Calling close handle with string</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28640](28640-----function---delayload-stub-should-be-a-static-function.md)</p></td>
<td align="left"><p>warning C28640: function delayload stub should be a static function</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28644](c28644.md)</p></td>
<td align="left"><p>warning C28644: Return value from DPA_InsertPtr not checked</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28645](28645---messagebox-was-called-using-the-question-mark-message-symbol-w.md)</p></td>
<td align="left"><p>warning C28645: MessageBox was called using the question mark message symbol which is no longer recommended</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28648](28648---pulseevent-is-an-unreliable-function--do-not-use-it.md)</p></td>
<td align="left"><p>warning C28648: PulseEvent is an unreliable function</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28649](28649---automatic-or-global-stack-arrays-are-never-null--checking-that.md)</p></td>
<td align="left"><p>warning C28649: Automatic or Global Stack Arrays are never NULL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28650](28650---the-type-for-which--0-is-being-used-does-not-treat-it-as-failu.md)</p></td>
<td align="left"><p>warning C28650: The type for which !0 is being used does not treat it as failure case.</p>
<p>Returning a status value such as !TRUE is not the same as returning a status value that indicates failure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28651](c28651.md)</p></td>
<td align="left"><p>warning C28651: Static initializer causes copy on write pages due to member function pointers</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28652](c28652.md)</p></td>
<td align="left"><p>warning C28652: Static initializer causes copy on write pages due to overloaded bitwise operators</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28714](28714---cast-between-semantically-different-integer-types--ntstatus-to.md)</p></td>
<td align="left"><p>warning C28714: Cast between semantically different integer types</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28715](28715---cast-between-semantically-different-integer-types--boolean-to-.md)</p></td>
<td align="left"><p>warning C28715: Cast between semantically different integer types</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28716](28716---compiler-inserted-cast-between-semantically-different-integral.md)</p></td>
<td align="left"><p>warning C28716: Compiler-inserted cast between semantically different integral types</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28717](28717---invalid-variant-type.md)</p></td>
<td align="left"><p>warning C28717: Invalid VARIANT type</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28718](c28718.md)</p></td>
<td align="left"><p>warning C28718: Unannotated buffer</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28719](28719---banned-api-usage----function--is-a-banned-api-as-listed-in-don.md)</p></td>
<td align="left"><p>warning C28719: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28720](28720---banned-api-usage---function--is-a-banned-api-as-listed-in-dont.md)</p></td>
<td align="left"><p>warning C28720: Banned API Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28721](28721----deprecated-performance-counter-architecture.md)</p></td>
<td align="left"><p>warning C28721: Deprecated performance counter architecture</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28722](c28722.md)</p></td>
<td align="left"><p>warning C28722: Unannotated buffer in function declaration</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28723](c28723.md)</p></td>
<td align="left"><p>warning C28723: Unannotated buffer in function definition that has no corresponding declaration</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28725](c28725.md)</p></td>
<td align="left"><p>warning C28725: Use Watson instead of this SetUnhandledExceptionFilter</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28726](28726---banned-api-usage---function--is-a-banned-api-as-listed-in-dont.md)</p></td>
<td align="left"><p>warning C28726: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28727](28727---banned-api-usage---function--is-a-banned-api-as-listed-in-dont.md)</p></td>
<td align="left"><p>warning C28727: Banned API Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28728](28728---banned-api-usage---function--is-a-banned-api-as-listed-in-dont.md)</p></td>
<td align="left"><p>warning C28728: Banned API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28730](28730---possible-assignment-of---0--directly-to-a-pointer--p---0--shou.md)</p></td>
<td align="left"><p>warning C28730: Possible assignment of '\\0' directly to a pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28735](28735---banned-crimson-api-usage----function--is-a-banned-crimson-api.md)</p></td>
<td align="left"><p>warning C28735: Banned Crimson API Usage</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28736](28736---banned-api-argument-usage---function--has-a-banned-crimson--or.md)</p></td>
<td align="left"><p>warning C28736: Banned API Argument Usage</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28740](c28740.md)</p></td>
<td align="left"><p>warning C28740: Unannotated unsigned buffer</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28741](c28741.md)</p></td>
<td align="left"><p>warning C28741: Unannotated buffer in the function</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28742](c28742.md)</p></td>
<td align="left"><p>warning C28742: Unannotated buffer in the function</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28750](c28750.md)</p></td>
<td align="left"><p>warning C28750: Banned usage of lstrlen and its variants</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28751](c28751.md)</p></td>
<td align="left"><p>warning C28751: Banned usage of ExAllocatePool and its variants</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C28752](c28752.md)</p></td>
<td align="left"><p>warning C28752: Banned usage of kernel32 or advapi32 API</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C28753](c28753.md)</p></td>
<td align="left"><p>warning C28753: Relying on undefined order of evaluation of parameters</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C30029](c30029.md)</p></td>
<td align="left"><p>warning C30029: Calling a memory allocating function that requests executable memory</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C30030](c30030.md)</p></td>
<td align="left"><p>warning C30030: Calling a memory allocating function and passing a parameter that indicates executable memory</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C30031](c30031.md)</p></td>
<td align="left"><p>warning C30031: Calling a memory allocating function and passing a parameter that indicates executable memory</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C30032](c30032.md)</p></td>
<td align="left"><p>warning C30032: Calling a memory allocating function and forcing the request of executable memory through use of the [POOL_NX_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401) directive</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C30033](c30033.md)</p></td>
<td align="left"><p>warning C30033: Executable allocation was detected in a driver compiled with [POOL_NX_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402). This driver has been determined to be loaded at run time by another driver. Please verify that the loading driver calls <strong>ExInitializeDriverRuntime(<em>DrvRtPoolNxOptIn</em>)</strong> in its DriverEntry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[C30034](c30034.md)</p></td>
<td align="left"><p>warning C30034: Passing a flag value to an allocating function that could result in executable memory being allocated. Please verify that the allocating function is not requesting a form of executable nonpaged pool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[C30035](c30035.md)</p></td>
<td align="left"><p>warning C30035: A call was made to a function that must be made from inside the initialization function (for example, <strong>DriverEntry()</strong> or <strong>DllInitialize()</strong>). PREfast was unable to determine if the call was made from the initialization function.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Code%20Analysis%20for%20Drivers%20Warnings%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




