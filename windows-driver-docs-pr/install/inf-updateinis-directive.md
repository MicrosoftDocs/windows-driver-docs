---
title: INF UpdateInis Directive
description: An UpdateInis directive specifies an INI file from which to read a section to be applied to an existing INI file of the same name on a target computer.
ms.assetid: c4717b6c-dc2d-45ba-8b39-3fc33e49466e
keywords:
- INF UpdateInis Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF UpdateInis Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF UpdateInis Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

An **UpdateInis** directive references one or more named sections, specifying an INI file from which a particular section or line is to be read and applied to an existing INI file of the same name on the target computer. Optionally, line-by-line modifications from and to such INI files can be specified in the *update-ini-section*.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows)
  
UpdateInis=update-ini-section[,update-ini-section]...
```

This directive is almost never specified in INF files for installation on Windows, due to the lack of necessity for INI files. However, the **UpdateInis** directive is valid in any of the sections shown in the formal syntax statement, as well as in INF-writer-defined sections referenced by an **AddInterface** directive or referenced in an **InterfaceInstall32** section.

Each named section referenced by an **UpdateInis** directive has the following form:

```cpp
[update-ini-section]
 
ini-file,ini-section[,old-ini-entry][,new-ini-entry][,flags]
...
```

An *update-ini-section* can have any INF-writer-determined number of entries, each on a separate line.

## Entries


<a href="" id="ini-file"></a>*ini-file*  
Specifies the name of an INI file supplied on the source media and, implicitly, that of the INI file to be updated on the target computer. This value can be expressed as a *filename* or as a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file.

<a href="" id="ini-section"></a>*ini-section*  
Specifies the name of the section within the given INI file. If the next two values are specified, this section contains an entry to be changed. If an *old-ini-entry* is omitted but a *new-ini-entry* is provided, the new entry is to be added as this section is read.

<a href="" id="old-ini-entry"></a>*old-ini-entry*  
This optional value specifies the name of an entry in the given *ini-section*, usually expressed in the following form:

```cpp
"key=value"
```

Either or both of *key* and *value* can be expressed as %*strkey*% tokens defined in a **Strings** section of the INF file. The asterisk (**\\**<em>) can be specified as a wild-card for either the *key</em> or the *value*.

<a href="" id="new-ini-entry"></a>*new-ini-entry*  
This optional value specifies either a change to a given *old-ini-entry* or the addition of a new entry. This value can be expressed in the same manner as *old-ini-entry*.

<a href="" id="flags"></a>*flags*  
This optional value controls the interpretation of the given *old-ini-entry* and/or *new-ini-entry*. The *flags* entry can be one of the following numeric values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>0</strong></td>
<td align="left"><p>This is the default value for the <em>flags</em> entry if it is omitted.</p>
<p>If the given <em>old-ini-entry</em> key is present in the INI files, replace that <em>key=value</em> with the given new-ini-entry. Only the keys in the INI files must match. The corresponding value of each such key is ignored.</p>
<p>To add a <em>new-ini-entry</em> to the destination INI file unconditionally, omit the <em>old-ini-entry</em> value from the entry in the <em>update-ini</em> section of the INF.</p>
<p>To delete an old-ini-entry from the destination INI file unconditionally, omit the <em>new-ini-entry</em> value.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>1</strong></td>
<td align="left"><p>If the given <em>old-ini-entry</em> (<em>key=value</em>) exists in the INI files, replace it in the destination INI file that has the given <em>new-ini-entry</em>. Both the <em>key</em> and <em>value</em> of the specified <em>old-ini-entry</em> must match those in the INI files for such a replacement to be made, not just their keys as for the preceding <em>flags</em> value.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>2</strong></td>
<td align="left"><p>If the <em>key</em> that is specified for <em>old-ini-entry</em> cannot be found in the destination INI file, do nothing. Otherwise, the changes made depend on matches found in the INI files for the given keys of <em>old-ini-entry</em> and <em>new-ini-entry</em>, as follows:</p>
<ol>
<li><p>If the <em>key</em> of the <em>old-ini-entry</em> exists in the INI files but so does the <em>key</em> of the <em>new-ini-entry</em>, replace the old-ini-entry with the <em>new-ini-entry</em> in the destination INI file and, then, remove the superfluous <em>new-ini-entry</em> from that INI file.</p></li>
<li><p>If the <em>key</em> of the <em>old-ini-entry</em> exists in the INI files but the key of the <em>new-ini-entry</em> does not, replace the <em>old-ini-entry</em>  <em>key</em> with that of the <em>new-ini-entry</em> in the destination INI file but leave the value of the <em>old-ini-entry</em> unchanged.</p></li>
</ol></td>
</tr>
<tr class="even">
<td align="left"><strong>3</strong></td>
<td align="left"><p>If the <em>key</em> and <em>value</em> specified for <em>old-ini-entry</em> cannot be found in the INI files, do nothing. Otherwise, the changes made depend on matches found in the INI files for the given <em>keys</em> and <em>values</em> of <em>old-ini-entry</em> and <em>new-ini-entry</em>, as follows:</p>
<ol>
<li><p>If the <em>key=value</em> of the <em>old-ini-entry</em> exists in the INI files but so does the <em>key=value</em> of the <em>new-ini-entry</em>, replace the <em>old-ini-entry</em> with the <em>new-ini-entry</em> in the destination INI file and, then, remove the superfluous <em>new-ini-entry</em> from that INI file.</p></li>
<li><p>If the <em>key=value</em> of the <em>old-ini-entry</em> exists in the INI files but the <em>new-ini-entry</em> does not, replace the <em>old-ini-entry</em> with the <em>new-ini-entry</em> in the destination INI file but leave the value of the <em>old-ini-entry</em> unchanged.</p></li>
</ol></td>
</tr>
</tbody>
</table>

 

Remarks
-------

A given *update-ini-section* name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The INF provides the full path of the given *ini-file* on the distribution media in one of the following ways:

-   In IHV/OEM-supplied INF files, by using the [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections of this INF to explicitly specify the full path of each named source file that is not in the root directory (or directories) on the distribution media.
-   In system-supplied INF files, by supplying one or more additional INF files, identified in the **LayoutFile** entry in the [**Version**](inf-version-section.md) section of the INF file.

Any *filename* specified within an *old-ini-entry* or *new-ini-entry* should designate the destination directory that contains that file. Such a destination directory path of a *filename* in an *update-ini-section* entry must be specified as a *dirid*. For lists of possible *dirid* values, see [Using Dirids](using-dirids.md).

## See also


[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**ProfileItems**](inf-profileitems-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**Version**](inf-version-section.md)

 

 






