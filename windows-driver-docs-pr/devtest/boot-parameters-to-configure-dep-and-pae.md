---
title: Boot Parameters to Configure DEP and PAE
description: Boot Parameters to Configure DEP and PAE
ms.assetid: cb8b6298-e679-4ca3-8b94-4f0c6af23a3f
keywords:
- boot parameters WDK
- boot entry parameters WDK
- DEP WDK boot parameters
- Data Execution Prevention WDK boot parameters
- Physical Address Extention WDK boot parameters
- PAE WDK boot parameters
- hardware-enforced DEP WDK boot parameters
- software-enforced DEP WDK boot parameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Boot Parameters to Configure DEP and PAE


This topic explains how to use boot parameters to enable, disable, and configure Data Execution Prevention (DEP) and Physical Address Extension (PAE) on operating systems that support these features.

For information about the boot parameters for DEP and PAE see the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command and the **nx** and **pae** options.

**Important**  DEP is a highly effective security feature that should not be disabled unless you have no alternative. The default settings for DEP and PAE are optimal for most systems. Do not change the default settings unless they interfere with essential processing tasks. This section is included to show you how to configure these features, but it should not be interpreted as a recommendation to change the default settings.

 

### <span id="dep_and_pae_boot_parameters"></span><span id="DEP_AND_PAE_BOOT_PARAMETERS"></span>DEP and PAE Boot Parameters

DEP and PAE are enabled at boot time and are configured by setting values for the **nx** and **pae** parameters using the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command.

These boot parameters have conflicting effects. To configure DEP and PAE, use only the parameter combinations that are described in the documentation for each parameter and discussed in this topic. Do not experiment with conflicting parameters, especially on a production system.

### <span id="the_interaction_of_dep_and_pae_boot_parameters"></span><span id="THE_INTERACTION_OF_DEP_AND_PAE_BOOT_PARAMETERS"></span>The Interaction of DEP and PAE Boot Parameters

There are two types of DEP:

-   *Hardware-enforced DEP* enables DEP for both kernel-mode and user-mode processes. It must be supported by the processor and the operating system.

<!-- -->

-   *Software-enforced DEP* enables DEP only on user-mode processes. It must be supported by the operating system.

On 32-bit versions of Windows, *hardware-enforced DEP* requires PAE, which is supported by all Windows operating systems that support DEP. When DEP is enabled on a computer with a processor that supports hardware-enforced DEP, Windows automatically enables PAE and ignores the boot parameter values that disable it.

The parameter combinations for each Windows operating system are summarized in the following section.

### <span id="dep_and_pae_parameter_combinations"></span><span id="DEP_AND_PAE_PARAMETER_COMBINATIONS"></span>DEP and PAE Parameter Combinations

The following list describes the boot parameter combinations that can be used to configure DEP and PAE.

**Note**   The optional **{**<em>ID</em>**}** is the GUID for the specific Windows boot loader boot entry that you want to configure. If you do not specify an **{**<em>ID</em>**}**, the command modifies the current operating system boot entry. For more information, see the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command .

 

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Action</th>
<th align="left"></th>
<th align="left">Windows Vista and later</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>To enable DEP</strong></p>
<p>(Select one parameter combination)</p>
<p>When DEP is enabled on computers that support hardware-enforced DEP, these parameter combinations also enable PAE.</p></td>
<td align="left"></td>
<td align="left"><p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx AlwaysOn</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx OptIn</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx OptOut</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>To enable DEP and PAE on systems with software-enforced DEP</strong></p>
<p>(Select one parameter combination)</p>
<p>On computers that support hardware-enforced DEP, PAE is automatically enabled when you enable DEP.</p></td>
<td align="left"></td>
<td align="left"><p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx AlwaysOn</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae default</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx OptIn</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae default</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx OptOut</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae default</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>To disable DEP, but enable PAE</strong></p></td>
<td align="left"></td>
<td align="left"><p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx AlwaysOff</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae ForceEnable</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>To disable DEP, but enable PAE</strong></p></td>
<td align="left"></td>
<td align="left"><p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx AlwaysOff</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae ForceEnable</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>To disable both DEP and PAE</strong></p></td>
<td align="left"></td>
<td align="left"><p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>nx AlwaysOff</strong></p>
<p><strong>/set</strong> [<strong>{</strong><em>ID</em><strong>}</strong>] <strong>pae ForceDisable</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>To disable both DEP and PAE</strong></p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

 

 





