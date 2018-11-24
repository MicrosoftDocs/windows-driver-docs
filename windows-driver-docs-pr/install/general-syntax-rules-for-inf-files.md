---
title: General Syntax Rules for INF Files
description: General Syntax Rules for INF Files
ms.assetid: ba11a229-d0d3-4217-bcf8-9aada2f159aa
keywords:
- INF files WDK device installations , general syntax rules
- INF files WDK device installations , sections
- sections WDK INF files
- INF files WDK device installations , directives
- directives WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Syntax Rules for INF Files





An INF file is a text file organized into named sections. Some sections have system-defined names and some sections have names determined by the writer of the INF file.

Each section contains section-specific entries that are interpreted by [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) (class installers, co-installers, SetupAPI). Some entries begin with a predefined keyword. These entries are called *directives*.

Some INF file entries are basically pointers from one section to another, for a specific purpose. For example, an [**INF AddReg directive**](inf-addreg-directive.md) identifies a section that contains entries that instruct Windows to modify the registry. These entries sometimes include additional arguments (required or optional) for Windows to interpret during installation.

Other INF file entries do not point to other sections, but supply information that Windows uses during installation, such as file names, registry values, hardware configuration information, flags, and so on. For example, an [**INF DriverVer directive**](inf-driverver-directive.md) supplies driver version information.

When Windows begins an installation, it first looks for an [**INF Version section**](inf-version-section.md) to verify the validity of the INF file and to determine where installation files are located. Then it starts the installation by finding an [**INF Manufacturer section**](inf-manufacturer-section.md). This section contains directives to [**INF *Models* sections**](inf-models-section.md), which in turn provide directives leading to various [**INF *DDInstall* sections**](inf-ddinstall-section.md), based on the hardware ID of the device being installed.

The following syntax rules govern the required and optional contents of INF files, the format of section names by using string tokens, and line format, continuation, and comments.

### <a href="" id="case-sensitivity"></a> Case Sensitivity

-   Section names, entries, and directives are case-insensitive. For example, **version**, **VERSION**, and **Version** are equally valid section name specifications within an INF file.

### <a href="" id="required-and-optional-contents"></a> Required and Optional Contents

- The set of required and optional sections, entries, and directives in any particular INF file depends on the type of device/driver or component (such as an application or device class installer DLL) to be installed.

- The set of sections, section-specific entries, and directives required to install any particular device and its drivers also depends somewhat on the corresponding class installer. For more information about how the system-supplied class installers handle device-type-specific INF files, see the device-type specific documentation in the WDK.

- Within syntax definitions, optional entries are delimited by *unbolded* brackets (\[,\]). On the other hand, *bold* brackets (**\[**, **\]**) are required elements of the entry in which they are contained. In the following example, the brackets around **Version** are required, while the brackets around **Class**=*class-name* indicate this entry is optional.

  <pre>
  <b>[</b>Version<b>]</b>

  Signature="signature-name"
  [Class=class-name]
  ...
  </pre>

### <a href="" id="section-names"></a> Section Names

- Sections can be specified in any order. Most INF files list sections in a particular order, by convention, but Windows finds sections by name, not by location within the INF file.

- Each section in an INF file begins with the section name enclosed in brackets (**\[ \]**). The section name can be system-defined or INF-writer-defined.

  For example, **\[Manufacturer\]** specifies the start of the system-named **Manufacturer** section, while <strong>\[</strong>Std.Mfg<strong>\]</strong> represents a particular INF-writer-defined *Models* section name.

  A section name has a maximum length of 255 characters on Windows 2000 and later versions of Windows.

  Each section ends at the beginning of a new **\[**<em>section-name</em>**\]** or at the end-of-file mark.

- If more than one section in an INF file has the same name, the system merges their entries and directives into a single section.

- Unless it is enclosed in double quotation marks characters (**"**), an INF-writer-defined section name must be a unique-to-the-INF unquoted string of explicitly visible characters, excluding certain characters with INF-specific meanings. In particular, an unquoted section name referenced by a section entry or directive cannot have leading or trailing spaces, a linefeed character, a return character, or any invisible control character, and it should not contain tabs. In addition, it cannot contain either of the bracket (**\[ \]**) characters, a single percent (**%**) character, a semicolon (**;**), or any internal double quotation marks (**"**) characters, and it cannot have a backslash (**\\**) as its last character.

  For example, Std.Mfg and Std_Mfg are unique and valid section names when referenced by an INF file entry or directive, but Std;Mfg (with its internal semicolon) is invalid unless it is enclosed by double quotation marks (**"**).

  Specifying an INF-writer-defined section name as a **"**<em>quoted string</em>**"** overrides most of the restrictions that were previously described on characters in referenced section names. Such a delimited section name can contain almost any explicitly or implicitly visible characters except the closing bracket (**\]**) as long as the corresponding section in the INF file matches this **"**<em>quoted string</em>**"** exactly.

  For example, **"**;; Std Mfg **"** is a valid section-name reference if the corresponding section declaration in the INF file exactly matches the name inside the double quotation marks with respect to its space and semicolon characters as **\[**;; Std Mfg **\]**.

### <a href="" id="using-string-tokens"></a> Using String Tokens

- Many values in an INF file, including INF-writer-defined section names, can be expressed as string key tokens of the form **%**<em>strkey</em>**%**. In the INF **Strings** section of the INF file, each string key must be associated with a string value that consists of a sequence of explicitly visible characters. If necessary, the setup code converts the string value, into Unicode.

  For more information about how to define **%**<em>strkey</em>**%** tokens and their respective values, see the description of the [**INF Strings section**](inf-strings-section.md).

### <a href="" id="line-format--continuation--and-comments"></a> Line Format, Continuation, and Comments

- Each entry and directive in a section ends with a return or linefeed character. Therefore, the text editor used to create an INF file must not insert return or linefeed characters after some arbitrary, editor-determined number of characters.

- The backslash character (**\\**) can be used as an explicit line continuator in an entry or directive. However, backslash characters are used also in path specifications. To ensure that a backslash character that appears in a path specification is not misinterpreted as a line continuator, use the following strategy:

  -   For a directive that spans two lines, one of which is an entry that contains a backslash, use quotation marks to delimit the entry that contains the backslash.

      ```cpp
      CopyFiles = "SomeDirectory\"\
      ,SomeFile
      ```

  -   Avoid using the backslash character in the manner shown in the following example. Windows ignores the first backslash and interprets the second backslash as a line continuator.

      ```cpp
      CopyFiles = SomeDirectory\\
      ,SomeFile
      ```

  -   The following syntax is valid and is equivalent to `CopyFiles = "SomeDirectory\",SomeFile ; comment`.

      ```cpp
      CopyFiles = "SomeDirectory\"\ ; comment 
      ,SomeFile
      ```
      Because text after a semicolon is ignored, `CopyFiles = "SomeDirectory\" ; comment ,SomeFile` does not work.

- Comments begin with a semicolon (**;**) character. When parsing and interpreting an INF file, the system assumes that the following have no relevance to the installation process:
  - Any characters following a semicolon on the same line, unless the semicolon appears within a **"**<em>quoted string</em>**"** or **%**<em>strkey</em>**%** token
  - Any empty line that contains nothing except a linefeed or return character

- Commas separate the values supplied in section entries and directives.

  An INF file entry or directive can omit an optional value in the middle of a list of values, but the commas must remain. INF files can omit trailing commas.

  For example, consider the syntax for a **SourceDisksFiles** section entry:

  <em>filename</em>**=**<em>diskid</em>\[**,**\[*subdir*\]\[**,**<em>size</em>\]\]

  An entry that omits the *subdir* value but supplies the *size* value must specify the comma delimiters for both values, as shown in the following example:

  <em>filename</em>**=**<em>diskid</em>**,,**<em>size</em>

  An entry in an INF file that omits the two optional values can have this format:

  <em>filename</em>**=**<em>diskid</em>
- In order to include a percent (%) character in values supplied in section entries and directives, escape the percent character with another percent character.

  For example, consider this statement in an *[add-registry-section]* section:

  *HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll"*

  The registry value will be set with the following value:

  *%SystemRoot%\System32\IoLogMsg.dll*
- In order to include a double quote (") character in values supplied in section entries and directives, escape the double quote character with another double quote character.  Note that the string must be within a **"**<em>quoted string</em>**"**.  

  For example, consider this statement in an *[add-registry-section]* section:

  *HKR,,Example,,"Display an ""example"" string"*

  The registry value will be set with the following value:

  *Display an "example" string*

### <a href="" id="inf-size-limits"></a> INF Size Limits

-   The maximum length, in characters, of an INF file field, before string substitution and including a terminating NULL character, is 4096.

-   After string substitution, the maximum length, in characters, of an INF file string is 4096, which includes a terminating NULL character.

-   However, be aware that Plug and Play (PnP) may impose a more restrictive limit for certain INF file fields that it recognizes or uses, such as device description, driver provider, and device manufacturer.









