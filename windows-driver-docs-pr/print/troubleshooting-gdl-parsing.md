---
title: Troubleshooting GDL Parsing
description: Troubleshooting GDL Parsing
ms.assetid: 8c678a2f-b15b-4693-9bed-0edec06b3485
keywords:
- GDL WDK , parser
- parser WDK GDL , troubleshooting parsing
- parsing GDL data WDK
- troubleshooting GDL parsing WDK
- GDL WDK , parsing errors
- GDL WDK , errors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting GDL Parsing


The following information covers some of the causes of unexpected behaviors that you might encounter when parsing GDL files.

<a href="" id="symptom--you-include-the-schema-file--but-the-parser-emits-an-error-message-that-says---no--root--template-found--gdl-entries-will-not-be--templatized--and-ignores-the-schema---"></a>Symptom: You include the schema file, but the parser emits an error message that says "no 'ROOT' template found, GDL entries will not be templatized" and ignores the schema.   
Solution: Check to see if a ROOT template is defined. If such a template is defined, ensure that the \#Include: schema.gdl directive comes before any instance data. Otherwise, the parser will ignore the schema.

<a href="" id="symptom--you-define-an-attribute-multiples-times-in-the-gdl-file--and-i-see-it-appear-in-the-xml-snapshot-only-once---"></a>Symptom: You define an attribute multiples times in the GDL file, and I see it appear in the XML snapshot only once.   
Solution: You must define a template for any attribute that appears in the XML snapshot multiple times. You must define the \*Additive directive. Otherwise, only the most recent definition will appear.

<a href="" id="symptom---the-parser-complains-that---production-defined-in-template----template-name---is-not-satisfied-by-actual-construct-----and-it-appears-that-the-number-of-occurrences-of-each-member-is-within-the-bounds-that-the-production-defines-"></a>Symptom: The parser complains that "\[Production defined in Template: "{template name}" is not satisfied by actual construct.\]", and it appears that the number of occurrences of each member is within the bounds that the production defines.  
Solution: First, check what template is bound to each GDL entry by using the -i option of the GDL parser. The binding might not have occurred the way that you anticipated. If the binding appears to have worked, remember that the production is satisfied by an instance of the template that named in the production and by any instance of any template that is derived from the named template. So, if the production specifies that only one instance of a particular template might be present and if the actual data file contains two instances of a template that derived from that template, the production will be violated. The template inheritance is tracked even if the derived template redefines the \*Name directive.

<a href="" id="symptom--you-receive-a-warning-message-that-references-an--invalidcombination-that-does-not-exist-in-the-gdl-file-that-is-being-parsed-"></a>Symptom: You receive a warning message that references an \*InvalidCombination that does not exist in the GDL file that is being parsed.  
Solution: The GDL parser converts \*Constraint directives into \*InvalidCombination directives internally. So, when errors are detected after conversion, the message refers to the \*Constraint as an \*InvalidCombination. Also, the order that each element of an \*InvalidCombination is stored in internally is not necessarily the order that is specified in the GDL file.

<a href="" id="symptom--spurious-trailing-space-appears-when-a-value-macro-reference-is-replaced-with-its-defined-value-"></a>Symptom: Spurious trailing space appears when a value macro reference is replaced with its defined value.  
Solution: The value macro definition contains a trailing comment. Move the comment to a separate line. In most contexts, the parser is insensitive to the presence of additional space characters.

<a href="" id="symptom---surrounding-non-conforming-syntax-with-a--ignoreblock-construct-does-not-hide-the-content-from-the-parser-as-syntax-errors-are-still-generated-"></a>Symptom: Surrounding non-conforming syntax with a \*IgnoreBlock construct does not hide the content from the Parser as syntax errors are still generated.  
Solution: The contents of \*IgnoreBlock must still be conforming GDL. \*IgnoreBlock will just prevent its contents from appearing in the internal data trees and prevent any non-preprocessor directives from being executed. To truly hide something, use preprocessor conditionals. If the fragment that is being hidden itself contains preprocessor directives that should not be executed, change the preprocessor prefix just before enclosing the fragment with preprocessor conditionals.

<a href="" id="symptom---features--constructs--and-attributes-that-are-defined-within-files-that-are-designated-with--precompiled-do-not-appear-in-the-xml-snapshot-and-cannot-be-referenced-by-the-host-file-"></a>Symptom: Features, constructs, and attributes that are defined within files that are designated with \*PreCompiled do not appear in the XML snapshot and cannot be referenced by the host file.  
Solution: This symptom occurs by design. You can store only templates and macro definitions within precompiled files.

<a href="" id="symptom---you-cannot-reference-templates--preprocessor-defines--macros--or-other-content-that-is-defined-elsewhere-from-within-files-that-are-designated-with--precompiled--"></a>Symptom: You cannot reference templates, preprocessor defines, macros, or other content that is defined elsewhere from within files that are designated with \*PreCompiled.   
Solution: This symptom occurs by design. Precompiled files are designed to be self-contained and completely independent of the host file's context. To access templates or other content that is defined in another file, you must place an \#Include directive that names that file directly within the \#PreCompiled file. Content that is indirectly included by virtue of being included (by using \#Include) within the \#Include file (that is, nested \#Include statements) will be accessible by the root precompiled (\#PreCompiled) file. Precompiled files can include (by using \#Include) other precompiled files.

<a href="" id="symptom---features-or-options-do-not-appear-in-the-snapshot-in-the-order-that-you-defined-them---or--the-first-option-is-not-assigned-as-the-default-option---"></a>Symptom: Features or options do not appear in the snapshot in the order that you defined them. Or, the first option is not assigned as the default option.   
Solution: Some options might have been defined previously in another part of the GDL file or in an included file that was processed before the feature or option definition that you are looking at. The first option that is processed becomes the first option, the second option that is processed becomes the second option in the snapshot, and so on.

<a href="" id="symptom--you-receive-a-warning-message-that-says-that-the-gdl-parser-cannot-find-a-template-that-is-referenced-by-the--elementtype-directive--but-that-template-is-defined--"></a>Symptom: You receive a warning message that says that the GDL parser cannot find a template that is referenced by the \*ElementType directive, but that template is defined.   
Solution: Only templates that are declared as \*Type: DATATYPE can be referenced by the \*ElementType directive.

<a href="" id="symptom--values-of-attributes-that-are-defined-to-be--filtertypename---codepage-string--are-not-converted-to-unicode-properly---"></a>Symptom: Values of attributes that are defined to be \*FilterTypeName: "CODEPAGE\_STRING" are not converted to Unicode properly.   
Solution: If the \*CodePage directive is not defined at the time this attribute is parsed, the parser assumes the string is already in Unicode. Make sure the \*CodePage definition appears before any CODEPAGE\_STRING attributes.

<a href="" id="symptom--you-defined-the--requireddelimiter-in-your-array-or-composite-data-type-template-to-be-a-sequence-of-multiple-space-characters-or-tabs--and-the-parser-does-not-seem-to-recognize-the-actual-data-even-though-it-conforms-exactly-to-the-template-definition---"></a>Symptom: You defined the \*RequiredDelimiter in your array or composite data type template to be a sequence of multiple space characters or tabs, and the parser does not seem to recognize the actual data even though it conforms exactly to the template definition.   
Solution: The parser internally converts any arbitrary string of whitespace (space or tab characters) into a single space character. So when the value is checked, it will not satisfy the template definition. To avoid this situation, specify only one space character for the \*RequiredDelimiter, or use a non-whitespace character for the \*RequiredDelimiter and use the space and tab characters for the \*OptionalDelimiter.

<a href="" id="symptom--dom-interface---xpath-query-cannot-find-any-elements-in-the-snapshot---for-example--selectsinglenode---snapshotroot-gdl-attribute----returns-nothing--"></a>Symptom: DOM interface: Xpath Query cannot find any elements in the snapshot (for example, selectSingleNode("/SnapshotRoot/GDL\_ATTRIBUTE") returns nothing).  
Solution: Xpath assumes that element names without a namespace prefix refer to the null or empty namespace, not the default namespace. The snapshot defines a default namespace and most elements belong to the default namespace.

To access these elements by using Xpath, the client must first map this default namespace to an explict prefix. To map the default namespace in this way, use the document pbjects setProperty method. The property that needs to be set is SelectionNamespaces. Use this property to assign the default namespace an explict prefix. In the snapshot, the default namespace is http://schemas.microsoft.com/2002/print/gdl/1.0 so the call to setProperty might look like the following code example.

```cpp
XMLDoc->setProperty(L"SelectionNamespaces", "xmlns:gdl=\"http://schemas.microsoft.com/2002/print/gdl/1.0\"");
```

The second argument in the preceding example is actually a Variant, but this added complexity is omitted for simplicity. The Xpath query must now explicitly reference the namespace prefix gdl when referencing elements in the default namespace. The query then becomes the following code example.

```cpp
selectSingleNode("/gdl:SnapshotRoot/gdl:GDL_ATTRIBUTE")
```

<a href="" id="symptom--the-dom-interface---nodetypedvalue-property-always-returns-values-as-bstr-types--regardless-of-their-xsi-type--"></a>Symptom: The DOM interface: nodeTypedValue property always returns values as BSTR types, regardless of their xsi:type.   
Solution: The current implementation of MSXML 4.0 recognizes only data types when they are defined by using a data type definition (DTD). The GDL parser uses XSD, which is the current W3C recommendation.

<a href="" id="symptom--quoted-strings-that-contain-characters-with-ansi-values-between-0-and-0x19-cause-xml-parsing-errors---except-for-0x0a--0x0d--and-0x09--"></a>Symptom: Quoted strings that contain characters with ANSI values between 0 and 0x19 cause XML parsing errors (except for 0x0a, 0x0d, and 0x09).  
Solution: This error is an XML feature. Such strings must be represented by using XML's binary or binhex data formats. Future versions of XML might accept strings that contain these characters.

<a href="" id="symptom--some-xml-instance-data-or-schema-that-are-defined-by-using-the-passthrough-or-xsd-defined-data-types-cause-xml-parser-or-validation-error-messages-when-loaded-into-dom-"></a>Symptom: Some XML instance data or schema that are defined by using the PASSTHROUGH or XSD\_DEFINED data types cause XML parser or validation error messages when loaded into DOM.  
Solution: Creating your own XML by using the PASSTHROUGH or XSD\_DEFINED data types bypasses the GDL parsers XML generation code and exposes you to the intricacies of XML and quirks in the DOM parser. You should be proficient enough with XML to deal with such problems before using these data types.

<a href="" id="symptom---the-parser-says--preface-cannot-be-used-with-a-precompiled-file---but-the-root-file-does-not-contain-a--precompiled-directive-"></a>Symptom: The parser says "Preface cannot be used with a precompiled file", but the root file does not contain a \#Precompiled directive.  
Solution: The \#Precompiled directive might actually reside in the preface itself. The parser cannot distinguish whether GDL content came from the preface or the root file.

 

 




