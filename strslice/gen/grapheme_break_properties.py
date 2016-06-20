# Auto-generated file, do not edit manually
# Re-generate using the `strslice-generate` command
# Unicode Version 8.0.0


def get(num):
    if 0x000D == num:
        return "CR"
    if 0x000A == num:
        return "LF"
    if 0x0000 <= num <= 0x0009:
        return "Control"
    if 0x000B <= num <= 0x000C:
        return "Control"
    if 0x000E <= num <= 0x001F:
        return "Control"
    if 0x007F <= num <= 0x009F:
        return "Control"
    if 0x00AD == num:
        return "Control"
    if 0x0600 <= num <= 0x0605:
        return "Control"
    if 0x061C == num:
        return "Control"
    if 0x06DD == num:
        return "Control"
    if 0x070F == num:
        return "Control"
    if 0x180E == num:
        return "Control"
    if 0x200B == num:
        return "Control"
    if 0x200E <= num <= 0x200F:
        return "Control"
    if 0x2028 == num:
        return "Control"
    if 0x2029 == num:
        return "Control"
    if 0x202A <= num <= 0x202E:
        return "Control"
    if 0x2060 <= num <= 0x2064:
        return "Control"
    if 0x2065 == num:
        return "Control"
    if 0x2066 <= num <= 0x206F:
        return "Control"
    if 0xD800 <= num <= 0xDFFF:
        return "Control"
    if 0xFEFF == num:
        return "Control"
    if 0xFFF0 <= num <= 0xFFF8:
        return "Control"
    if 0xFFF9 <= num <= 0xFFFB:
        return "Control"
    if 0x110BD == num:
        return "Control"
    if 0x1BCA0 <= num <= 0x1BCA3:
        return "Control"
    if 0x1D173 <= num <= 0x1D17A:
        return "Control"
    if 0xE0000 == num:
        return "Control"
    if 0xE0001 == num:
        return "Control"
    if 0xE0002 <= num <= 0xE001F:
        return "Control"
    if 0xE0020 <= num <= 0xE007F:
        return "Control"
    if 0xE0080 <= num <= 0xE00FF:
        return "Control"
    if 0xE01F0 <= num <= 0xE0FFF:
        return "Control"
    if 0x0300 <= num <= 0x036F:
        return "Extend"
    if 0x0483 <= num <= 0x0487:
        return "Extend"
    if 0x0488 <= num <= 0x0489:
        return "Extend"
    if 0x0591 <= num <= 0x05BD:
        return "Extend"
    if 0x05BF == num:
        return "Extend"
    if 0x05C1 <= num <= 0x05C2:
        return "Extend"
    if 0x05C4 <= num <= 0x05C5:
        return "Extend"
    if 0x05C7 == num:
        return "Extend"
    if 0x0610 <= num <= 0x061A:
        return "Extend"
    if 0x064B <= num <= 0x065F:
        return "Extend"
    if 0x0670 == num:
        return "Extend"
    if 0x06D6 <= num <= 0x06DC:
        return "Extend"
    if 0x06DF <= num <= 0x06E4:
        return "Extend"
    if 0x06E7 <= num <= 0x06E8:
        return "Extend"
    if 0x06EA <= num <= 0x06ED:
        return "Extend"
    if 0x0711 == num:
        return "Extend"
    if 0x0730 <= num <= 0x074A:
        return "Extend"
    if 0x07A6 <= num <= 0x07B0:
        return "Extend"
    if 0x07EB <= num <= 0x07F3:
        return "Extend"
    if 0x0816 <= num <= 0x0819:
        return "Extend"
    if 0x081B <= num <= 0x0823:
        return "Extend"
    if 0x0825 <= num <= 0x0827:
        return "Extend"
    if 0x0829 <= num <= 0x082D:
        return "Extend"
    if 0x0859 <= num <= 0x085B:
        return "Extend"
    if 0x08E3 <= num <= 0x0902:
        return "Extend"
    if 0x093A == num:
        return "Extend"
    if 0x093C == num:
        return "Extend"
    if 0x0941 <= num <= 0x0948:
        return "Extend"
    if 0x094D == num:
        return "Extend"
    if 0x0951 <= num <= 0x0957:
        return "Extend"
    if 0x0962 <= num <= 0x0963:
        return "Extend"
    if 0x0981 == num:
        return "Extend"
    if 0x09BC == num:
        return "Extend"
    if 0x09BE == num:
        return "Extend"
    if 0x09C1 <= num <= 0x09C4:
        return "Extend"
    if 0x09CD == num:
        return "Extend"
    if 0x09D7 == num:
        return "Extend"
    if 0x09E2 <= num <= 0x09E3:
        return "Extend"
    if 0x0A01 <= num <= 0x0A02:
        return "Extend"
    if 0x0A3C == num:
        return "Extend"
    if 0x0A41 <= num <= 0x0A42:
        return "Extend"
    if 0x0A47 <= num <= 0x0A48:
        return "Extend"
    if 0x0A4B <= num <= 0x0A4D:
        return "Extend"
    if 0x0A51 == num:
        return "Extend"
    if 0x0A70 <= num <= 0x0A71:
        return "Extend"
    if 0x0A75 == num:
        return "Extend"
    if 0x0A81 <= num <= 0x0A82:
        return "Extend"
    if 0x0ABC == num:
        return "Extend"
    if 0x0AC1 <= num <= 0x0AC5:
        return "Extend"
    if 0x0AC7 <= num <= 0x0AC8:
        return "Extend"
    if 0x0ACD == num:
        return "Extend"
    if 0x0AE2 <= num <= 0x0AE3:
        return "Extend"
    if 0x0B01 == num:
        return "Extend"
    if 0x0B3C == num:
        return "Extend"
    if 0x0B3E == num:
        return "Extend"
    if 0x0B3F == num:
        return "Extend"
    if 0x0B41 <= num <= 0x0B44:
        return "Extend"
    if 0x0B4D == num:
        return "Extend"
    if 0x0B56 == num:
        return "Extend"
    if 0x0B57 == num:
        return "Extend"
    if 0x0B62 <= num <= 0x0B63:
        return "Extend"
    if 0x0B82 == num:
        return "Extend"
    if 0x0BBE == num:
        return "Extend"
    if 0x0BC0 == num:
        return "Extend"
    if 0x0BCD == num:
        return "Extend"
    if 0x0BD7 == num:
        return "Extend"
    if 0x0C00 == num:
        return "Extend"
    if 0x0C3E <= num <= 0x0C40:
        return "Extend"
    if 0x0C46 <= num <= 0x0C48:
        return "Extend"
    if 0x0C4A <= num <= 0x0C4D:
        return "Extend"
    if 0x0C55 <= num <= 0x0C56:
        return "Extend"
    if 0x0C62 <= num <= 0x0C63:
        return "Extend"
    if 0x0C81 == num:
        return "Extend"
    if 0x0CBC == num:
        return "Extend"
    if 0x0CBF == num:
        return "Extend"
    if 0x0CC2 == num:
        return "Extend"
    if 0x0CC6 == num:
        return "Extend"
    if 0x0CCC <= num <= 0x0CCD:
        return "Extend"
    if 0x0CD5 <= num <= 0x0CD6:
        return "Extend"
    if 0x0CE2 <= num <= 0x0CE3:
        return "Extend"
    if 0x0D01 == num:
        return "Extend"
    if 0x0D3E == num:
        return "Extend"
    if 0x0D41 <= num <= 0x0D44:
        return "Extend"
    if 0x0D4D == num:
        return "Extend"
    if 0x0D57 == num:
        return "Extend"
    if 0x0D62 <= num <= 0x0D63:
        return "Extend"
    if 0x0DCA == num:
        return "Extend"
    if 0x0DCF == num:
        return "Extend"
    if 0x0DD2 <= num <= 0x0DD4:
        return "Extend"
    if 0x0DD6 == num:
        return "Extend"
    if 0x0DDF == num:
        return "Extend"
    if 0x0E31 == num:
        return "Extend"
    if 0x0E34 <= num <= 0x0E3A:
        return "Extend"
    if 0x0E47 <= num <= 0x0E4E:
        return "Extend"
    if 0x0EB1 == num:
        return "Extend"
    if 0x0EB4 <= num <= 0x0EB9:
        return "Extend"
    if 0x0EBB <= num <= 0x0EBC:
        return "Extend"
    if 0x0EC8 <= num <= 0x0ECD:
        return "Extend"
    if 0x0F18 <= num <= 0x0F19:
        return "Extend"
    if 0x0F35 == num:
        return "Extend"
    if 0x0F37 == num:
        return "Extend"
    if 0x0F39 == num:
        return "Extend"
    if 0x0F71 <= num <= 0x0F7E:
        return "Extend"
    if 0x0F80 <= num <= 0x0F84:
        return "Extend"
    if 0x0F86 <= num <= 0x0F87:
        return "Extend"
    if 0x0F8D <= num <= 0x0F97:
        return "Extend"
    if 0x0F99 <= num <= 0x0FBC:
        return "Extend"
    if 0x0FC6 == num:
        return "Extend"
    if 0x102D <= num <= 0x1030:
        return "Extend"
    if 0x1032 <= num <= 0x1037:
        return "Extend"
    if 0x1039 <= num <= 0x103A:
        return "Extend"
    if 0x103D <= num <= 0x103E:
        return "Extend"
    if 0x1058 <= num <= 0x1059:
        return "Extend"
    if 0x105E <= num <= 0x1060:
        return "Extend"
    if 0x1071 <= num <= 0x1074:
        return "Extend"
    if 0x1082 == num:
        return "Extend"
    if 0x1085 <= num <= 0x1086:
        return "Extend"
    if 0x108D == num:
        return "Extend"
    if 0x109D == num:
        return "Extend"
    if 0x135D <= num <= 0x135F:
        return "Extend"
    if 0x1712 <= num <= 0x1714:
        return "Extend"
    if 0x1732 <= num <= 0x1734:
        return "Extend"
    if 0x1752 <= num <= 0x1753:
        return "Extend"
    if 0x1772 <= num <= 0x1773:
        return "Extend"
    if 0x17B4 <= num <= 0x17B5:
        return "Extend"
    if 0x17B7 <= num <= 0x17BD:
        return "Extend"
    if 0x17C6 == num:
        return "Extend"
    if 0x17C9 <= num <= 0x17D3:
        return "Extend"
    if 0x17DD == num:
        return "Extend"
    if 0x180B <= num <= 0x180D:
        return "Extend"
    if 0x18A9 == num:
        return "Extend"
    if 0x1920 <= num <= 0x1922:
        return "Extend"
    if 0x1927 <= num <= 0x1928:
        return "Extend"
    if 0x1932 == num:
        return "Extend"
    if 0x1939 <= num <= 0x193B:
        return "Extend"
    if 0x1A17 <= num <= 0x1A18:
        return "Extend"
    if 0x1A1B == num:
        return "Extend"
    if 0x1A56 == num:
        return "Extend"
    if 0x1A58 <= num <= 0x1A5E:
        return "Extend"
    if 0x1A60 == num:
        return "Extend"
    if 0x1A62 == num:
        return "Extend"
    if 0x1A65 <= num <= 0x1A6C:
        return "Extend"
    if 0x1A73 <= num <= 0x1A7C:
        return "Extend"
    if 0x1A7F == num:
        return "Extend"
    if 0x1AB0 <= num <= 0x1ABD:
        return "Extend"
    if 0x1ABE == num:
        return "Extend"
    if 0x1B00 <= num <= 0x1B03:
        return "Extend"
    if 0x1B34 == num:
        return "Extend"
    if 0x1B36 <= num <= 0x1B3A:
        return "Extend"
    if 0x1B3C == num:
        return "Extend"
    if 0x1B42 == num:
        return "Extend"
    if 0x1B6B <= num <= 0x1B73:
        return "Extend"
    if 0x1B80 <= num <= 0x1B81:
        return "Extend"
    if 0x1BA2 <= num <= 0x1BA5:
        return "Extend"
    if 0x1BA8 <= num <= 0x1BA9:
        return "Extend"
    if 0x1BAB <= num <= 0x1BAD:
        return "Extend"
    if 0x1BE6 == num:
        return "Extend"
    if 0x1BE8 <= num <= 0x1BE9:
        return "Extend"
    if 0x1BED == num:
        return "Extend"
    if 0x1BEF <= num <= 0x1BF1:
        return "Extend"
    if 0x1C2C <= num <= 0x1C33:
        return "Extend"
    if 0x1C36 <= num <= 0x1C37:
        return "Extend"
    if 0x1CD0 <= num <= 0x1CD2:
        return "Extend"
    if 0x1CD4 <= num <= 0x1CE0:
        return "Extend"
    if 0x1CE2 <= num <= 0x1CE8:
        return "Extend"
    if 0x1CED == num:
        return "Extend"
    if 0x1CF4 == num:
        return "Extend"
    if 0x1CF8 <= num <= 0x1CF9:
        return "Extend"
    if 0x1DC0 <= num <= 0x1DF5:
        return "Extend"
    if 0x1DFC <= num <= 0x1DFF:
        return "Extend"
    if 0x200C <= num <= 0x200D:
        return "Extend"
    if 0x20D0 <= num <= 0x20DC:
        return "Extend"
    if 0x20DD <= num <= 0x20E0:
        return "Extend"
    if 0x20E1 == num:
        return "Extend"
    if 0x20E2 <= num <= 0x20E4:
        return "Extend"
    if 0x20E5 <= num <= 0x20F0:
        return "Extend"
    if 0x2CEF <= num <= 0x2CF1:
        return "Extend"
    if 0x2D7F == num:
        return "Extend"
    if 0x2DE0 <= num <= 0x2DFF:
        return "Extend"
    if 0x302A <= num <= 0x302D:
        return "Extend"
    if 0x302E <= num <= 0x302F:
        return "Extend"
    if 0x3099 <= num <= 0x309A:
        return "Extend"
    if 0xA66F == num:
        return "Extend"
    if 0xA670 <= num <= 0xA672:
        return "Extend"
    if 0xA674 <= num <= 0xA67D:
        return "Extend"
    if 0xA69E <= num <= 0xA69F:
        return "Extend"
    if 0xA6F0 <= num <= 0xA6F1:
        return "Extend"
    if 0xA802 == num:
        return "Extend"
    if 0xA806 == num:
        return "Extend"
    if 0xA80B == num:
        return "Extend"
    if 0xA825 <= num <= 0xA826:
        return "Extend"
    if 0xA8C4 == num:
        return "Extend"
    if 0xA8E0 <= num <= 0xA8F1:
        return "Extend"
    if 0xA926 <= num <= 0xA92D:
        return "Extend"
    if 0xA947 <= num <= 0xA951:
        return "Extend"
    if 0xA980 <= num <= 0xA982:
        return "Extend"
    if 0xA9B3 == num:
        return "Extend"
    if 0xA9B6 <= num <= 0xA9B9:
        return "Extend"
    if 0xA9BC == num:
        return "Extend"
    if 0xA9E5 == num:
        return "Extend"
    if 0xAA29 <= num <= 0xAA2E:
        return "Extend"
    if 0xAA31 <= num <= 0xAA32:
        return "Extend"
    if 0xAA35 <= num <= 0xAA36:
        return "Extend"
    if 0xAA43 == num:
        return "Extend"
    if 0xAA4C == num:
        return "Extend"
    if 0xAA7C == num:
        return "Extend"
    if 0xAAB0 == num:
        return "Extend"
    if 0xAAB2 <= num <= 0xAAB4:
        return "Extend"
    if 0xAAB7 <= num <= 0xAAB8:
        return "Extend"
    if 0xAABE <= num <= 0xAABF:
        return "Extend"
    if 0xAAC1 == num:
        return "Extend"
    if 0xAAEC <= num <= 0xAAED:
        return "Extend"
    if 0xAAF6 == num:
        return "Extend"
    if 0xABE5 == num:
        return "Extend"
    if 0xABE8 == num:
        return "Extend"
    if 0xABED == num:
        return "Extend"
    if 0xFB1E == num:
        return "Extend"
    if 0xFE00 <= num <= 0xFE0F:
        return "Extend"
    if 0xFE20 <= num <= 0xFE2F:
        return "Extend"
    if 0xFF9E <= num <= 0xFF9F:
        return "Extend"
    if 0x101FD == num:
        return "Extend"
    if 0x102E0 == num:
        return "Extend"
    if 0x10376 <= num <= 0x1037A:
        return "Extend"
    if 0x10A01 <= num <= 0x10A03:
        return "Extend"
    if 0x10A05 <= num <= 0x10A06:
        return "Extend"
    if 0x10A0C <= num <= 0x10A0F:
        return "Extend"
    if 0x10A38 <= num <= 0x10A3A:
        return "Extend"
    if 0x10A3F == num:
        return "Extend"
    if 0x10AE5 <= num <= 0x10AE6:
        return "Extend"
    if 0x11001 == num:
        return "Extend"
    if 0x11038 <= num <= 0x11046:
        return "Extend"
    if 0x1107F <= num <= 0x11081:
        return "Extend"
    if 0x110B3 <= num <= 0x110B6:
        return "Extend"
    if 0x110B9 <= num <= 0x110BA:
        return "Extend"
    if 0x11100 <= num <= 0x11102:
        return "Extend"
    if 0x11127 <= num <= 0x1112B:
        return "Extend"
    if 0x1112D <= num <= 0x11134:
        return "Extend"
    if 0x11173 == num:
        return "Extend"
    if 0x11180 <= num <= 0x11181:
        return "Extend"
    if 0x111B6 <= num <= 0x111BE:
        return "Extend"
    if 0x111CA <= num <= 0x111CC:
        return "Extend"
    if 0x1122F <= num <= 0x11231:
        return "Extend"
    if 0x11234 == num:
        return "Extend"
    if 0x11236 <= num <= 0x11237:
        return "Extend"
    if 0x112DF == num:
        return "Extend"
    if 0x112E3 <= num <= 0x112EA:
        return "Extend"
    if 0x11300 <= num <= 0x11301:
        return "Extend"
    if 0x1133C == num:
        return "Extend"
    if 0x1133E == num:
        return "Extend"
    if 0x11340 == num:
        return "Extend"
    if 0x11357 == num:
        return "Extend"
    if 0x11366 <= num <= 0x1136C:
        return "Extend"
    if 0x11370 <= num <= 0x11374:
        return "Extend"
    if 0x114B0 == num:
        return "Extend"
    if 0x114B3 <= num <= 0x114B8:
        return "Extend"
    if 0x114BA == num:
        return "Extend"
    if 0x114BD == num:
        return "Extend"
    if 0x114BF <= num <= 0x114C0:
        return "Extend"
    if 0x114C2 <= num <= 0x114C3:
        return "Extend"
    if 0x115AF == num:
        return "Extend"
    if 0x115B2 <= num <= 0x115B5:
        return "Extend"
    if 0x115BC <= num <= 0x115BD:
        return "Extend"
    if 0x115BF <= num <= 0x115C0:
        return "Extend"
    if 0x115DC <= num <= 0x115DD:
        return "Extend"
    if 0x11633 <= num <= 0x1163A:
        return "Extend"
    if 0x1163D == num:
        return "Extend"
    if 0x1163F <= num <= 0x11640:
        return "Extend"
    if 0x116AB == num:
        return "Extend"
    if 0x116AD == num:
        return "Extend"
    if 0x116B0 <= num <= 0x116B5:
        return "Extend"
    if 0x116B7 == num:
        return "Extend"
    if 0x1171D <= num <= 0x1171F:
        return "Extend"
    if 0x11722 <= num <= 0x11725:
        return "Extend"
    if 0x11727 <= num <= 0x1172B:
        return "Extend"
    if 0x16AF0 <= num <= 0x16AF4:
        return "Extend"
    if 0x16B30 <= num <= 0x16B36:
        return "Extend"
    if 0x16F8F <= num <= 0x16F92:
        return "Extend"
    if 0x1BC9D <= num <= 0x1BC9E:
        return "Extend"
    if 0x1D165 == num:
        return "Extend"
    if 0x1D167 <= num <= 0x1D169:
        return "Extend"
    if 0x1D16E <= num <= 0x1D172:
        return "Extend"
    if 0x1D17B <= num <= 0x1D182:
        return "Extend"
    if 0x1D185 <= num <= 0x1D18B:
        return "Extend"
    if 0x1D1AA <= num <= 0x1D1AD:
        return "Extend"
    if 0x1D242 <= num <= 0x1D244:
        return "Extend"
    if 0x1DA00 <= num <= 0x1DA36:
        return "Extend"
    if 0x1DA3B <= num <= 0x1DA6C:
        return "Extend"
    if 0x1DA75 == num:
        return "Extend"
    if 0x1DA84 == num:
        return "Extend"
    if 0x1DA9B <= num <= 0x1DA9F:
        return "Extend"
    if 0x1DAA1 <= num <= 0x1DAAF:
        return "Extend"
    if 0x1E8D0 <= num <= 0x1E8D6:
        return "Extend"
    if 0xE0100 <= num <= 0xE01EF:
        return "Extend"
    if 0x1F1E6 <= num <= 0x1F1FF:
        return "Regional_Indicator"
    if 0x0903 == num:
        return "SpacingMark"
    if 0x093B == num:
        return "SpacingMark"
    if 0x093E <= num <= 0x0940:
        return "SpacingMark"
    if 0x0949 <= num <= 0x094C:
        return "SpacingMark"
    if 0x094E <= num <= 0x094F:
        return "SpacingMark"
    if 0x0982 <= num <= 0x0983:
        return "SpacingMark"
    if 0x09BF <= num <= 0x09C0:
        return "SpacingMark"
    if 0x09C7 <= num <= 0x09C8:
        return "SpacingMark"
    if 0x09CB <= num <= 0x09CC:
        return "SpacingMark"
    if 0x0A03 == num:
        return "SpacingMark"
    if 0x0A3E <= num <= 0x0A40:
        return "SpacingMark"
    if 0x0A83 == num:
        return "SpacingMark"
    if 0x0ABE <= num <= 0x0AC0:
        return "SpacingMark"
    if 0x0AC9 == num:
        return "SpacingMark"
    if 0x0ACB <= num <= 0x0ACC:
        return "SpacingMark"
    if 0x0B02 <= num <= 0x0B03:
        return "SpacingMark"
    if 0x0B40 == num:
        return "SpacingMark"
    if 0x0B47 <= num <= 0x0B48:
        return "SpacingMark"
    if 0x0B4B <= num <= 0x0B4C:
        return "SpacingMark"
    if 0x0BBF == num:
        return "SpacingMark"
    if 0x0BC1 <= num <= 0x0BC2:
        return "SpacingMark"
    if 0x0BC6 <= num <= 0x0BC8:
        return "SpacingMark"
    if 0x0BCA <= num <= 0x0BCC:
        return "SpacingMark"
    if 0x0C01 <= num <= 0x0C03:
        return "SpacingMark"
    if 0x0C41 <= num <= 0x0C44:
        return "SpacingMark"
    if 0x0C82 <= num <= 0x0C83:
        return "SpacingMark"
    if 0x0CBE == num:
        return "SpacingMark"
    if 0x0CC0 <= num <= 0x0CC1:
        return "SpacingMark"
    if 0x0CC3 <= num <= 0x0CC4:
        return "SpacingMark"
    if 0x0CC7 <= num <= 0x0CC8:
        return "SpacingMark"
    if 0x0CCA <= num <= 0x0CCB:
        return "SpacingMark"
    if 0x0D02 <= num <= 0x0D03:
        return "SpacingMark"
    if 0x0D3F <= num <= 0x0D40:
        return "SpacingMark"
    if 0x0D46 <= num <= 0x0D48:
        return "SpacingMark"
    if 0x0D4A <= num <= 0x0D4C:
        return "SpacingMark"
    if 0x0D82 <= num <= 0x0D83:
        return "SpacingMark"
    if 0x0DD0 <= num <= 0x0DD1:
        return "SpacingMark"
    if 0x0DD8 <= num <= 0x0DDE:
        return "SpacingMark"
    if 0x0DF2 <= num <= 0x0DF3:
        return "SpacingMark"
    if 0x0E33 == num:
        return "SpacingMark"
    if 0x0EB3 == num:
        return "SpacingMark"
    if 0x0F3E <= num <= 0x0F3F:
        return "SpacingMark"
    if 0x0F7F == num:
        return "SpacingMark"
    if 0x1031 == num:
        return "SpacingMark"
    if 0x103B <= num <= 0x103C:
        return "SpacingMark"
    if 0x1056 <= num <= 0x1057:
        return "SpacingMark"
    if 0x1084 == num:
        return "SpacingMark"
    if 0x17B6 == num:
        return "SpacingMark"
    if 0x17BE <= num <= 0x17C5:
        return "SpacingMark"
    if 0x17C7 <= num <= 0x17C8:
        return "SpacingMark"
    if 0x1923 <= num <= 0x1926:
        return "SpacingMark"
    if 0x1929 <= num <= 0x192B:
        return "SpacingMark"
    if 0x1930 <= num <= 0x1931:
        return "SpacingMark"
    if 0x1933 <= num <= 0x1938:
        return "SpacingMark"
    if 0x1A19 <= num <= 0x1A1A:
        return "SpacingMark"
    if 0x1A55 == num:
        return "SpacingMark"
    if 0x1A57 == num:
        return "SpacingMark"
    if 0x1A6D <= num <= 0x1A72:
        return "SpacingMark"
    if 0x1B04 == num:
        return "SpacingMark"
    if 0x1B35 == num:
        return "SpacingMark"
    if 0x1B3B == num:
        return "SpacingMark"
    if 0x1B3D <= num <= 0x1B41:
        return "SpacingMark"
    if 0x1B43 <= num <= 0x1B44:
        return "SpacingMark"
    if 0x1B82 == num:
        return "SpacingMark"
    if 0x1BA1 == num:
        return "SpacingMark"
    if 0x1BA6 <= num <= 0x1BA7:
        return "SpacingMark"
    if 0x1BAA == num:
        return "SpacingMark"
    if 0x1BE7 == num:
        return "SpacingMark"
    if 0x1BEA <= num <= 0x1BEC:
        return "SpacingMark"
    if 0x1BEE == num:
        return "SpacingMark"
    if 0x1BF2 <= num <= 0x1BF3:
        return "SpacingMark"
    if 0x1C24 <= num <= 0x1C2B:
        return "SpacingMark"
    if 0x1C34 <= num <= 0x1C35:
        return "SpacingMark"
    if 0x1CE1 == num:
        return "SpacingMark"
    if 0x1CF2 <= num <= 0x1CF3:
        return "SpacingMark"
    if 0xA823 <= num <= 0xA824:
        return "SpacingMark"
    if 0xA827 == num:
        return "SpacingMark"
    if 0xA880 <= num <= 0xA881:
        return "SpacingMark"
    if 0xA8B4 <= num <= 0xA8C3:
        return "SpacingMark"
    if 0xA952 <= num <= 0xA953:
        return "SpacingMark"
    if 0xA983 == num:
        return "SpacingMark"
    if 0xA9B4 <= num <= 0xA9B5:
        return "SpacingMark"
    if 0xA9BA <= num <= 0xA9BB:
        return "SpacingMark"
    if 0xA9BD <= num <= 0xA9C0:
        return "SpacingMark"
    if 0xAA2F <= num <= 0xAA30:
        return "SpacingMark"
    if 0xAA33 <= num <= 0xAA34:
        return "SpacingMark"
    if 0xAA4D == num:
        return "SpacingMark"
    if 0xAAEB == num:
        return "SpacingMark"
    if 0xAAEE <= num <= 0xAAEF:
        return "SpacingMark"
    if 0xAAF5 == num:
        return "SpacingMark"
    if 0xABE3 <= num <= 0xABE4:
        return "SpacingMark"
    if 0xABE6 <= num <= 0xABE7:
        return "SpacingMark"
    if 0xABE9 <= num <= 0xABEA:
        return "SpacingMark"
    if 0xABEC == num:
        return "SpacingMark"
    if 0x11000 == num:
        return "SpacingMark"
    if 0x11002 == num:
        return "SpacingMark"
    if 0x11082 == num:
        return "SpacingMark"
    if 0x110B0 <= num <= 0x110B2:
        return "SpacingMark"
    if 0x110B7 <= num <= 0x110B8:
        return "SpacingMark"
    if 0x1112C == num:
        return "SpacingMark"
    if 0x11182 == num:
        return "SpacingMark"
    if 0x111B3 <= num <= 0x111B5:
        return "SpacingMark"
    if 0x111BF <= num <= 0x111C0:
        return "SpacingMark"
    if 0x1122C <= num <= 0x1122E:
        return "SpacingMark"
    if 0x11232 <= num <= 0x11233:
        return "SpacingMark"
    if 0x11235 == num:
        return "SpacingMark"
    if 0x112E0 <= num <= 0x112E2:
        return "SpacingMark"
    if 0x11302 <= num <= 0x11303:
        return "SpacingMark"
    if 0x1133F == num:
        return "SpacingMark"
    if 0x11341 <= num <= 0x11344:
        return "SpacingMark"
    if 0x11347 <= num <= 0x11348:
        return "SpacingMark"
    if 0x1134B <= num <= 0x1134D:
        return "SpacingMark"
    if 0x11362 <= num <= 0x11363:
        return "SpacingMark"
    if 0x114B1 <= num <= 0x114B2:
        return "SpacingMark"
    if 0x114B9 == num:
        return "SpacingMark"
    if 0x114BB <= num <= 0x114BC:
        return "SpacingMark"
    if 0x114BE == num:
        return "SpacingMark"
    if 0x114C1 == num:
        return "SpacingMark"
    if 0x115B0 <= num <= 0x115B1:
        return "SpacingMark"
    if 0x115B8 <= num <= 0x115BB:
        return "SpacingMark"
    if 0x115BE == num:
        return "SpacingMark"
    if 0x11630 <= num <= 0x11632:
        return "SpacingMark"
    if 0x1163B <= num <= 0x1163C:
        return "SpacingMark"
    if 0x1163E == num:
        return "SpacingMark"
    if 0x116AC == num:
        return "SpacingMark"
    if 0x116AE <= num <= 0x116AF:
        return "SpacingMark"
    if 0x116B6 == num:
        return "SpacingMark"
    if 0x11720 <= num <= 0x11721:
        return "SpacingMark"
    if 0x11726 == num:
        return "SpacingMark"
    if 0x16F51 <= num <= 0x16F7E:
        return "SpacingMark"
    if 0x1D166 == num:
        return "SpacingMark"
    if 0x1D16D == num:
        return "SpacingMark"
    if 0x1100 <= num <= 0x115F:
        return "L"
    if 0xA960 <= num <= 0xA97C:
        return "L"
    if 0x1160 <= num <= 0x11A7:
        return "V"
    if 0xD7B0 <= num <= 0xD7C6:
        return "V"
    if 0x11A8 <= num <= 0x11FF:
        return "T"
    if 0xD7CB <= num <= 0xD7FB:
        return "T"
    if 0xAC00 == num:
        return "LV"
    if 0xAC1C == num:
        return "LV"
    if 0xAC38 == num:
        return "LV"
    if 0xAC54 == num:
        return "LV"
    if 0xAC70 == num:
        return "LV"
    if 0xAC8C == num:
        return "LV"
    if 0xACA8 == num:
        return "LV"
    if 0xACC4 == num:
        return "LV"
    if 0xACE0 == num:
        return "LV"
    if 0xACFC == num:
        return "LV"
    if 0xAD18 == num:
        return "LV"
    if 0xAD34 == num:
        return "LV"
    if 0xAD50 == num:
        return "LV"
    if 0xAD6C == num:
        return "LV"
    if 0xAD88 == num:
        return "LV"
    if 0xADA4 == num:
        return "LV"
    if 0xADC0 == num:
        return "LV"
    if 0xADDC == num:
        return "LV"
    if 0xADF8 == num:
        return "LV"
    if 0xAE14 == num:
        return "LV"
    if 0xAE30 == num:
        return "LV"
    if 0xAE4C == num:
        return "LV"
    if 0xAE68 == num:
        return "LV"
    if 0xAE84 == num:
        return "LV"
    if 0xAEA0 == num:
        return "LV"
    if 0xAEBC == num:
        return "LV"
    if 0xAED8 == num:
        return "LV"
    if 0xAEF4 == num:
        return "LV"
    if 0xAF10 == num:
        return "LV"
    if 0xAF2C == num:
        return "LV"
    if 0xAF48 == num:
        return "LV"
    if 0xAF64 == num:
        return "LV"
    if 0xAF80 == num:
        return "LV"
    if 0xAF9C == num:
        return "LV"
    if 0xAFB8 == num:
        return "LV"
    if 0xAFD4 == num:
        return "LV"
    if 0xAFF0 == num:
        return "LV"
    if 0xB00C == num:
        return "LV"
    if 0xB028 == num:
        return "LV"
    if 0xB044 == num:
        return "LV"
    if 0xB060 == num:
        return "LV"
    if 0xB07C == num:
        return "LV"
    if 0xB098 == num:
        return "LV"
    if 0xB0B4 == num:
        return "LV"
    if 0xB0D0 == num:
        return "LV"
    if 0xB0EC == num:
        return "LV"
    if 0xB108 == num:
        return "LV"
    if 0xB124 == num:
        return "LV"
    if 0xB140 == num:
        return "LV"
    if 0xB15C == num:
        return "LV"
    if 0xB178 == num:
        return "LV"
    if 0xB194 == num:
        return "LV"
    if 0xB1B0 == num:
        return "LV"
    if 0xB1CC == num:
        return "LV"
    if 0xB1E8 == num:
        return "LV"
    if 0xB204 == num:
        return "LV"
    if 0xB220 == num:
        return "LV"
    if 0xB23C == num:
        return "LV"
    if 0xB258 == num:
        return "LV"
    if 0xB274 == num:
        return "LV"
    if 0xB290 == num:
        return "LV"
    if 0xB2AC == num:
        return "LV"
    if 0xB2C8 == num:
        return "LV"
    if 0xB2E4 == num:
        return "LV"
    if 0xB300 == num:
        return "LV"
    if 0xB31C == num:
        return "LV"
    if 0xB338 == num:
        return "LV"
    if 0xB354 == num:
        return "LV"
    if 0xB370 == num:
        return "LV"
    if 0xB38C == num:
        return "LV"
    if 0xB3A8 == num:
        return "LV"
    if 0xB3C4 == num:
        return "LV"
    if 0xB3E0 == num:
        return "LV"
    if 0xB3FC == num:
        return "LV"
    if 0xB418 == num:
        return "LV"
    if 0xB434 == num:
        return "LV"
    if 0xB450 == num:
        return "LV"
    if 0xB46C == num:
        return "LV"
    if 0xB488 == num:
        return "LV"
    if 0xB4A4 == num:
        return "LV"
    if 0xB4C0 == num:
        return "LV"
    if 0xB4DC == num:
        return "LV"
    if 0xB4F8 == num:
        return "LV"
    if 0xB514 == num:
        return "LV"
    if 0xB530 == num:
        return "LV"
    if 0xB54C == num:
        return "LV"
    if 0xB568 == num:
        return "LV"
    if 0xB584 == num:
        return "LV"
    if 0xB5A0 == num:
        return "LV"
    if 0xB5BC == num:
        return "LV"
    if 0xB5D8 == num:
        return "LV"
    if 0xB5F4 == num:
        return "LV"
    if 0xB610 == num:
        return "LV"
    if 0xB62C == num:
        return "LV"
    if 0xB648 == num:
        return "LV"
    if 0xB664 == num:
        return "LV"
    if 0xB680 == num:
        return "LV"
    if 0xB69C == num:
        return "LV"
    if 0xB6B8 == num:
        return "LV"
    if 0xB6D4 == num:
        return "LV"
    if 0xB6F0 == num:
        return "LV"
    if 0xB70C == num:
        return "LV"
    if 0xB728 == num:
        return "LV"
    if 0xB744 == num:
        return "LV"
    if 0xB760 == num:
        return "LV"
    if 0xB77C == num:
        return "LV"
    if 0xB798 == num:
        return "LV"
    if 0xB7B4 == num:
        return "LV"
    if 0xB7D0 == num:
        return "LV"
    if 0xB7EC == num:
        return "LV"
    if 0xB808 == num:
        return "LV"
    if 0xB824 == num:
        return "LV"
    if 0xB840 == num:
        return "LV"
    if 0xB85C == num:
        return "LV"
    if 0xB878 == num:
        return "LV"
    if 0xB894 == num:
        return "LV"
    if 0xB8B0 == num:
        return "LV"
    if 0xB8CC == num:
        return "LV"
    if 0xB8E8 == num:
        return "LV"
    if 0xB904 == num:
        return "LV"
    if 0xB920 == num:
        return "LV"
    if 0xB93C == num:
        return "LV"
    if 0xB958 == num:
        return "LV"
    if 0xB974 == num:
        return "LV"
    if 0xB990 == num:
        return "LV"
    if 0xB9AC == num:
        return "LV"
    if 0xB9C8 == num:
        return "LV"
    if 0xB9E4 == num:
        return "LV"
    if 0xBA00 == num:
        return "LV"
    if 0xBA1C == num:
        return "LV"
    if 0xBA38 == num:
        return "LV"
    if 0xBA54 == num:
        return "LV"
    if 0xBA70 == num:
        return "LV"
    if 0xBA8C == num:
        return "LV"
    if 0xBAA8 == num:
        return "LV"
    if 0xBAC4 == num:
        return "LV"
    if 0xBAE0 == num:
        return "LV"
    if 0xBAFC == num:
        return "LV"
    if 0xBB18 == num:
        return "LV"
    if 0xBB34 == num:
        return "LV"
    if 0xBB50 == num:
        return "LV"
    if 0xBB6C == num:
        return "LV"
    if 0xBB88 == num:
        return "LV"
    if 0xBBA4 == num:
        return "LV"
    if 0xBBC0 == num:
        return "LV"
    if 0xBBDC == num:
        return "LV"
    if 0xBBF8 == num:
        return "LV"
    if 0xBC14 == num:
        return "LV"
    if 0xBC30 == num:
        return "LV"
    if 0xBC4C == num:
        return "LV"
    if 0xBC68 == num:
        return "LV"
    if 0xBC84 == num:
        return "LV"
    if 0xBCA0 == num:
        return "LV"
    if 0xBCBC == num:
        return "LV"
    if 0xBCD8 == num:
        return "LV"
    if 0xBCF4 == num:
        return "LV"
    if 0xBD10 == num:
        return "LV"
    if 0xBD2C == num:
        return "LV"
    if 0xBD48 == num:
        return "LV"
    if 0xBD64 == num:
        return "LV"
    if 0xBD80 == num:
        return "LV"
    if 0xBD9C == num:
        return "LV"
    if 0xBDB8 == num:
        return "LV"
    if 0xBDD4 == num:
        return "LV"
    if 0xBDF0 == num:
        return "LV"
    if 0xBE0C == num:
        return "LV"
    if 0xBE28 == num:
        return "LV"
    if 0xBE44 == num:
        return "LV"
    if 0xBE60 == num:
        return "LV"
    if 0xBE7C == num:
        return "LV"
    if 0xBE98 == num:
        return "LV"
    if 0xBEB4 == num:
        return "LV"
    if 0xBED0 == num:
        return "LV"
    if 0xBEEC == num:
        return "LV"
    if 0xBF08 == num:
        return "LV"
    if 0xBF24 == num:
        return "LV"
    if 0xBF40 == num:
        return "LV"
    if 0xBF5C == num:
        return "LV"
    if 0xBF78 == num:
        return "LV"
    if 0xBF94 == num:
        return "LV"
    if 0xBFB0 == num:
        return "LV"
    if 0xBFCC == num:
        return "LV"
    if 0xBFE8 == num:
        return "LV"
    if 0xC004 == num:
        return "LV"
    if 0xC020 == num:
        return "LV"
    if 0xC03C == num:
        return "LV"
    if 0xC058 == num:
        return "LV"
    if 0xC074 == num:
        return "LV"
    if 0xC090 == num:
        return "LV"
    if 0xC0AC == num:
        return "LV"
    if 0xC0C8 == num:
        return "LV"
    if 0xC0E4 == num:
        return "LV"
    if 0xC100 == num:
        return "LV"
    if 0xC11C == num:
        return "LV"
    if 0xC138 == num:
        return "LV"
    if 0xC154 == num:
        return "LV"
    if 0xC170 == num:
        return "LV"
    if 0xC18C == num:
        return "LV"
    if 0xC1A8 == num:
        return "LV"
    if 0xC1C4 == num:
        return "LV"
    if 0xC1E0 == num:
        return "LV"
    if 0xC1FC == num:
        return "LV"
    if 0xC218 == num:
        return "LV"
    if 0xC234 == num:
        return "LV"
    if 0xC250 == num:
        return "LV"
    if 0xC26C == num:
        return "LV"
    if 0xC288 == num:
        return "LV"
    if 0xC2A4 == num:
        return "LV"
    if 0xC2C0 == num:
        return "LV"
    if 0xC2DC == num:
        return "LV"
    if 0xC2F8 == num:
        return "LV"
    if 0xC314 == num:
        return "LV"
    if 0xC330 == num:
        return "LV"
    if 0xC34C == num:
        return "LV"
    if 0xC368 == num:
        return "LV"
    if 0xC384 == num:
        return "LV"
    if 0xC3A0 == num:
        return "LV"
    if 0xC3BC == num:
        return "LV"
    if 0xC3D8 == num:
        return "LV"
    if 0xC3F4 == num:
        return "LV"
    if 0xC410 == num:
        return "LV"
    if 0xC42C == num:
        return "LV"
    if 0xC448 == num:
        return "LV"
    if 0xC464 == num:
        return "LV"
    if 0xC480 == num:
        return "LV"
    if 0xC49C == num:
        return "LV"
    if 0xC4B8 == num:
        return "LV"
    if 0xC4D4 == num:
        return "LV"
    if 0xC4F0 == num:
        return "LV"
    if 0xC50C == num:
        return "LV"
    if 0xC528 == num:
        return "LV"
    if 0xC544 == num:
        return "LV"
    if 0xC560 == num:
        return "LV"
    if 0xC57C == num:
        return "LV"
    if 0xC598 == num:
        return "LV"
    if 0xC5B4 == num:
        return "LV"
    if 0xC5D0 == num:
        return "LV"
    if 0xC5EC == num:
        return "LV"
    if 0xC608 == num:
        return "LV"
    if 0xC624 == num:
        return "LV"
    if 0xC640 == num:
        return "LV"
    if 0xC65C == num:
        return "LV"
    if 0xC678 == num:
        return "LV"
    if 0xC694 == num:
        return "LV"
    if 0xC6B0 == num:
        return "LV"
    if 0xC6CC == num:
        return "LV"
    if 0xC6E8 == num:
        return "LV"
    if 0xC704 == num:
        return "LV"
    if 0xC720 == num:
        return "LV"
    if 0xC73C == num:
        return "LV"
    if 0xC758 == num:
        return "LV"
    if 0xC774 == num:
        return "LV"
    if 0xC790 == num:
        return "LV"
    if 0xC7AC == num:
        return "LV"
    if 0xC7C8 == num:
        return "LV"
    if 0xC7E4 == num:
        return "LV"
    if 0xC800 == num:
        return "LV"
    if 0xC81C == num:
        return "LV"
    if 0xC838 == num:
        return "LV"
    if 0xC854 == num:
        return "LV"
    if 0xC870 == num:
        return "LV"
    if 0xC88C == num:
        return "LV"
    if 0xC8A8 == num:
        return "LV"
    if 0xC8C4 == num:
        return "LV"
    if 0xC8E0 == num:
        return "LV"
    if 0xC8FC == num:
        return "LV"
    if 0xC918 == num:
        return "LV"
    if 0xC934 == num:
        return "LV"
    if 0xC950 == num:
        return "LV"
    if 0xC96C == num:
        return "LV"
    if 0xC988 == num:
        return "LV"
    if 0xC9A4 == num:
        return "LV"
    if 0xC9C0 == num:
        return "LV"
    if 0xC9DC == num:
        return "LV"
    if 0xC9F8 == num:
        return "LV"
    if 0xCA14 == num:
        return "LV"
    if 0xCA30 == num:
        return "LV"
    if 0xCA4C == num:
        return "LV"
    if 0xCA68 == num:
        return "LV"
    if 0xCA84 == num:
        return "LV"
    if 0xCAA0 == num:
        return "LV"
    if 0xCABC == num:
        return "LV"
    if 0xCAD8 == num:
        return "LV"
    if 0xCAF4 == num:
        return "LV"
    if 0xCB10 == num:
        return "LV"
    if 0xCB2C == num:
        return "LV"
    if 0xCB48 == num:
        return "LV"
    if 0xCB64 == num:
        return "LV"
    if 0xCB80 == num:
        return "LV"
    if 0xCB9C == num:
        return "LV"
    if 0xCBB8 == num:
        return "LV"
    if 0xCBD4 == num:
        return "LV"
    if 0xCBF0 == num:
        return "LV"
    if 0xCC0C == num:
        return "LV"
    if 0xCC28 == num:
        return "LV"
    if 0xCC44 == num:
        return "LV"
    if 0xCC60 == num:
        return "LV"
    if 0xCC7C == num:
        return "LV"
    if 0xCC98 == num:
        return "LV"
    if 0xCCB4 == num:
        return "LV"
    if 0xCCD0 == num:
        return "LV"
    if 0xCCEC == num:
        return "LV"
    if 0xCD08 == num:
        return "LV"
    if 0xCD24 == num:
        return "LV"
    if 0xCD40 == num:
        return "LV"
    if 0xCD5C == num:
        return "LV"
    if 0xCD78 == num:
        return "LV"
    if 0xCD94 == num:
        return "LV"
    if 0xCDB0 == num:
        return "LV"
    if 0xCDCC == num:
        return "LV"
    if 0xCDE8 == num:
        return "LV"
    if 0xCE04 == num:
        return "LV"
    if 0xCE20 == num:
        return "LV"
    if 0xCE3C == num:
        return "LV"
    if 0xCE58 == num:
        return "LV"
    if 0xCE74 == num:
        return "LV"
    if 0xCE90 == num:
        return "LV"
    if 0xCEAC == num:
        return "LV"
    if 0xCEC8 == num:
        return "LV"
    if 0xCEE4 == num:
        return "LV"
    if 0xCF00 == num:
        return "LV"
    if 0xCF1C == num:
        return "LV"
    if 0xCF38 == num:
        return "LV"
    if 0xCF54 == num:
        return "LV"
    if 0xCF70 == num:
        return "LV"
    if 0xCF8C == num:
        return "LV"
    if 0xCFA8 == num:
        return "LV"
    if 0xCFC4 == num:
        return "LV"
    if 0xCFE0 == num:
        return "LV"
    if 0xCFFC == num:
        return "LV"
    if 0xD018 == num:
        return "LV"
    if 0xD034 == num:
        return "LV"
    if 0xD050 == num:
        return "LV"
    if 0xD06C == num:
        return "LV"
    if 0xD088 == num:
        return "LV"
    if 0xD0A4 == num:
        return "LV"
    if 0xD0C0 == num:
        return "LV"
    if 0xD0DC == num:
        return "LV"
    if 0xD0F8 == num:
        return "LV"
    if 0xD114 == num:
        return "LV"
    if 0xD130 == num:
        return "LV"
    if 0xD14C == num:
        return "LV"
    if 0xD168 == num:
        return "LV"
    if 0xD184 == num:
        return "LV"
    if 0xD1A0 == num:
        return "LV"
    if 0xD1BC == num:
        return "LV"
    if 0xD1D8 == num:
        return "LV"
    if 0xD1F4 == num:
        return "LV"
    if 0xD210 == num:
        return "LV"
    if 0xD22C == num:
        return "LV"
    if 0xD248 == num:
        return "LV"
    if 0xD264 == num:
        return "LV"
    if 0xD280 == num:
        return "LV"
    if 0xD29C == num:
        return "LV"
    if 0xD2B8 == num:
        return "LV"
    if 0xD2D4 == num:
        return "LV"
    if 0xD2F0 == num:
        return "LV"
    if 0xD30C == num:
        return "LV"
    if 0xD328 == num:
        return "LV"
    if 0xD344 == num:
        return "LV"
    if 0xD360 == num:
        return "LV"
    if 0xD37C == num:
        return "LV"
    if 0xD398 == num:
        return "LV"
    if 0xD3B4 == num:
        return "LV"
    if 0xD3D0 == num:
        return "LV"
    if 0xD3EC == num:
        return "LV"
    if 0xD408 == num:
        return "LV"
    if 0xD424 == num:
        return "LV"
    if 0xD440 == num:
        return "LV"
    if 0xD45C == num:
        return "LV"
    if 0xD478 == num:
        return "LV"
    if 0xD494 == num:
        return "LV"
    if 0xD4B0 == num:
        return "LV"
    if 0xD4CC == num:
        return "LV"
    if 0xD4E8 == num:
        return "LV"
    if 0xD504 == num:
        return "LV"
    if 0xD520 == num:
        return "LV"
    if 0xD53C == num:
        return "LV"
    if 0xD558 == num:
        return "LV"
    if 0xD574 == num:
        return "LV"
    if 0xD590 == num:
        return "LV"
    if 0xD5AC == num:
        return "LV"
    if 0xD5C8 == num:
        return "LV"
    if 0xD5E4 == num:
        return "LV"
    if 0xD600 == num:
        return "LV"
    if 0xD61C == num:
        return "LV"
    if 0xD638 == num:
        return "LV"
    if 0xD654 == num:
        return "LV"
    if 0xD670 == num:
        return "LV"
    if 0xD68C == num:
        return "LV"
    if 0xD6A8 == num:
        return "LV"
    if 0xD6C4 == num:
        return "LV"
    if 0xD6E0 == num:
        return "LV"
    if 0xD6FC == num:
        return "LV"
    if 0xD718 == num:
        return "LV"
    if 0xD734 == num:
        return "LV"
    if 0xD750 == num:
        return "LV"
    if 0xD76C == num:
        return "LV"
    if 0xD788 == num:
        return "LV"
    if 0xAC01 <= num <= 0xAC1B:
        return "LVT"
    if 0xAC1D <= num <= 0xAC37:
        return "LVT"
    if 0xAC39 <= num <= 0xAC53:
        return "LVT"
    if 0xAC55 <= num <= 0xAC6F:
        return "LVT"
    if 0xAC71 <= num <= 0xAC8B:
        return "LVT"
    if 0xAC8D <= num <= 0xACA7:
        return "LVT"
    if 0xACA9 <= num <= 0xACC3:
        return "LVT"
    if 0xACC5 <= num <= 0xACDF:
        return "LVT"
    if 0xACE1 <= num <= 0xACFB:
        return "LVT"
    if 0xACFD <= num <= 0xAD17:
        return "LVT"
    if 0xAD19 <= num <= 0xAD33:
        return "LVT"
    if 0xAD35 <= num <= 0xAD4F:
        return "LVT"
    if 0xAD51 <= num <= 0xAD6B:
        return "LVT"
    if 0xAD6D <= num <= 0xAD87:
        return "LVT"
    if 0xAD89 <= num <= 0xADA3:
        return "LVT"
    if 0xADA5 <= num <= 0xADBF:
        return "LVT"
    if 0xADC1 <= num <= 0xADDB:
        return "LVT"
    if 0xADDD <= num <= 0xADF7:
        return "LVT"
    if 0xADF9 <= num <= 0xAE13:
        return "LVT"
    if 0xAE15 <= num <= 0xAE2F:
        return "LVT"
    if 0xAE31 <= num <= 0xAE4B:
        return "LVT"
    if 0xAE4D <= num <= 0xAE67:
        return "LVT"
    if 0xAE69 <= num <= 0xAE83:
        return "LVT"
    if 0xAE85 <= num <= 0xAE9F:
        return "LVT"
    if 0xAEA1 <= num <= 0xAEBB:
        return "LVT"
    if 0xAEBD <= num <= 0xAED7:
        return "LVT"
    if 0xAED9 <= num <= 0xAEF3:
        return "LVT"
    if 0xAEF5 <= num <= 0xAF0F:
        return "LVT"
    if 0xAF11 <= num <= 0xAF2B:
        return "LVT"
    if 0xAF2D <= num <= 0xAF47:
        return "LVT"
    if 0xAF49 <= num <= 0xAF63:
        return "LVT"
    if 0xAF65 <= num <= 0xAF7F:
        return "LVT"
    if 0xAF81 <= num <= 0xAF9B:
        return "LVT"
    if 0xAF9D <= num <= 0xAFB7:
        return "LVT"
    if 0xAFB9 <= num <= 0xAFD3:
        return "LVT"
    if 0xAFD5 <= num <= 0xAFEF:
        return "LVT"
    if 0xAFF1 <= num <= 0xB00B:
        return "LVT"
    if 0xB00D <= num <= 0xB027:
        return "LVT"
    if 0xB029 <= num <= 0xB043:
        return "LVT"
    if 0xB045 <= num <= 0xB05F:
        return "LVT"
    if 0xB061 <= num <= 0xB07B:
        return "LVT"
    if 0xB07D <= num <= 0xB097:
        return "LVT"
    if 0xB099 <= num <= 0xB0B3:
        return "LVT"
    if 0xB0B5 <= num <= 0xB0CF:
        return "LVT"
    if 0xB0D1 <= num <= 0xB0EB:
        return "LVT"
    if 0xB0ED <= num <= 0xB107:
        return "LVT"
    if 0xB109 <= num <= 0xB123:
        return "LVT"
    if 0xB125 <= num <= 0xB13F:
        return "LVT"
    if 0xB141 <= num <= 0xB15B:
        return "LVT"
    if 0xB15D <= num <= 0xB177:
        return "LVT"
    if 0xB179 <= num <= 0xB193:
        return "LVT"
    if 0xB195 <= num <= 0xB1AF:
        return "LVT"
    if 0xB1B1 <= num <= 0xB1CB:
        return "LVT"
    if 0xB1CD <= num <= 0xB1E7:
        return "LVT"
    if 0xB1E9 <= num <= 0xB203:
        return "LVT"
    if 0xB205 <= num <= 0xB21F:
        return "LVT"
    if 0xB221 <= num <= 0xB23B:
        return "LVT"
    if 0xB23D <= num <= 0xB257:
        return "LVT"
    if 0xB259 <= num <= 0xB273:
        return "LVT"
    if 0xB275 <= num <= 0xB28F:
        return "LVT"
    if 0xB291 <= num <= 0xB2AB:
        return "LVT"
    if 0xB2AD <= num <= 0xB2C7:
        return "LVT"
    if 0xB2C9 <= num <= 0xB2E3:
        return "LVT"
    if 0xB2E5 <= num <= 0xB2FF:
        return "LVT"
    if 0xB301 <= num <= 0xB31B:
        return "LVT"
    if 0xB31D <= num <= 0xB337:
        return "LVT"
    if 0xB339 <= num <= 0xB353:
        return "LVT"
    if 0xB355 <= num <= 0xB36F:
        return "LVT"
    if 0xB371 <= num <= 0xB38B:
        return "LVT"
    if 0xB38D <= num <= 0xB3A7:
        return "LVT"
    if 0xB3A9 <= num <= 0xB3C3:
        return "LVT"
    if 0xB3C5 <= num <= 0xB3DF:
        return "LVT"
    if 0xB3E1 <= num <= 0xB3FB:
        return "LVT"
    if 0xB3FD <= num <= 0xB417:
        return "LVT"
    if 0xB419 <= num <= 0xB433:
        return "LVT"
    if 0xB435 <= num <= 0xB44F:
        return "LVT"
    if 0xB451 <= num <= 0xB46B:
        return "LVT"
    if 0xB46D <= num <= 0xB487:
        return "LVT"
    if 0xB489 <= num <= 0xB4A3:
        return "LVT"
    if 0xB4A5 <= num <= 0xB4BF:
        return "LVT"
    if 0xB4C1 <= num <= 0xB4DB:
        return "LVT"
    if 0xB4DD <= num <= 0xB4F7:
        return "LVT"
    if 0xB4F9 <= num <= 0xB513:
        return "LVT"
    if 0xB515 <= num <= 0xB52F:
        return "LVT"
    if 0xB531 <= num <= 0xB54B:
        return "LVT"
    if 0xB54D <= num <= 0xB567:
        return "LVT"
    if 0xB569 <= num <= 0xB583:
        return "LVT"
    if 0xB585 <= num <= 0xB59F:
        return "LVT"
    if 0xB5A1 <= num <= 0xB5BB:
        return "LVT"
    if 0xB5BD <= num <= 0xB5D7:
        return "LVT"
    if 0xB5D9 <= num <= 0xB5F3:
        return "LVT"
    if 0xB5F5 <= num <= 0xB60F:
        return "LVT"
    if 0xB611 <= num <= 0xB62B:
        return "LVT"
    if 0xB62D <= num <= 0xB647:
        return "LVT"
    if 0xB649 <= num <= 0xB663:
        return "LVT"
    if 0xB665 <= num <= 0xB67F:
        return "LVT"
    if 0xB681 <= num <= 0xB69B:
        return "LVT"
    if 0xB69D <= num <= 0xB6B7:
        return "LVT"
    if 0xB6B9 <= num <= 0xB6D3:
        return "LVT"
    if 0xB6D5 <= num <= 0xB6EF:
        return "LVT"
    if 0xB6F1 <= num <= 0xB70B:
        return "LVT"
    if 0xB70D <= num <= 0xB727:
        return "LVT"
    if 0xB729 <= num <= 0xB743:
        return "LVT"
    if 0xB745 <= num <= 0xB75F:
        return "LVT"
    if 0xB761 <= num <= 0xB77B:
        return "LVT"
    if 0xB77D <= num <= 0xB797:
        return "LVT"
    if 0xB799 <= num <= 0xB7B3:
        return "LVT"
    if 0xB7B5 <= num <= 0xB7CF:
        return "LVT"
    if 0xB7D1 <= num <= 0xB7EB:
        return "LVT"
    if 0xB7ED <= num <= 0xB807:
        return "LVT"
    if 0xB809 <= num <= 0xB823:
        return "LVT"
    if 0xB825 <= num <= 0xB83F:
        return "LVT"
    if 0xB841 <= num <= 0xB85B:
        return "LVT"
    if 0xB85D <= num <= 0xB877:
        return "LVT"
    if 0xB879 <= num <= 0xB893:
        return "LVT"
    if 0xB895 <= num <= 0xB8AF:
        return "LVT"
    if 0xB8B1 <= num <= 0xB8CB:
        return "LVT"
    if 0xB8CD <= num <= 0xB8E7:
        return "LVT"
    if 0xB8E9 <= num <= 0xB903:
        return "LVT"
    if 0xB905 <= num <= 0xB91F:
        return "LVT"
    if 0xB921 <= num <= 0xB93B:
        return "LVT"
    if 0xB93D <= num <= 0xB957:
        return "LVT"
    if 0xB959 <= num <= 0xB973:
        return "LVT"
    if 0xB975 <= num <= 0xB98F:
        return "LVT"
    if 0xB991 <= num <= 0xB9AB:
        return "LVT"
    if 0xB9AD <= num <= 0xB9C7:
        return "LVT"
    if 0xB9C9 <= num <= 0xB9E3:
        return "LVT"
    if 0xB9E5 <= num <= 0xB9FF:
        return "LVT"
    if 0xBA01 <= num <= 0xBA1B:
        return "LVT"
    if 0xBA1D <= num <= 0xBA37:
        return "LVT"
    if 0xBA39 <= num <= 0xBA53:
        return "LVT"
    if 0xBA55 <= num <= 0xBA6F:
        return "LVT"
    if 0xBA71 <= num <= 0xBA8B:
        return "LVT"
    if 0xBA8D <= num <= 0xBAA7:
        return "LVT"
    if 0xBAA9 <= num <= 0xBAC3:
        return "LVT"
    if 0xBAC5 <= num <= 0xBADF:
        return "LVT"
    if 0xBAE1 <= num <= 0xBAFB:
        return "LVT"
    if 0xBAFD <= num <= 0xBB17:
        return "LVT"
    if 0xBB19 <= num <= 0xBB33:
        return "LVT"
    if 0xBB35 <= num <= 0xBB4F:
        return "LVT"
    if 0xBB51 <= num <= 0xBB6B:
        return "LVT"
    if 0xBB6D <= num <= 0xBB87:
        return "LVT"
    if 0xBB89 <= num <= 0xBBA3:
        return "LVT"
    if 0xBBA5 <= num <= 0xBBBF:
        return "LVT"
    if 0xBBC1 <= num <= 0xBBDB:
        return "LVT"
    if 0xBBDD <= num <= 0xBBF7:
        return "LVT"
    if 0xBBF9 <= num <= 0xBC13:
        return "LVT"
    if 0xBC15 <= num <= 0xBC2F:
        return "LVT"
    if 0xBC31 <= num <= 0xBC4B:
        return "LVT"
    if 0xBC4D <= num <= 0xBC67:
        return "LVT"
    if 0xBC69 <= num <= 0xBC83:
        return "LVT"
    if 0xBC85 <= num <= 0xBC9F:
        return "LVT"
    if 0xBCA1 <= num <= 0xBCBB:
        return "LVT"
    if 0xBCBD <= num <= 0xBCD7:
        return "LVT"
    if 0xBCD9 <= num <= 0xBCF3:
        return "LVT"
    if 0xBCF5 <= num <= 0xBD0F:
        return "LVT"
    if 0xBD11 <= num <= 0xBD2B:
        return "LVT"
    if 0xBD2D <= num <= 0xBD47:
        return "LVT"
    if 0xBD49 <= num <= 0xBD63:
        return "LVT"
    if 0xBD65 <= num <= 0xBD7F:
        return "LVT"
    if 0xBD81 <= num <= 0xBD9B:
        return "LVT"
    if 0xBD9D <= num <= 0xBDB7:
        return "LVT"
    if 0xBDB9 <= num <= 0xBDD3:
        return "LVT"
    if 0xBDD5 <= num <= 0xBDEF:
        return "LVT"
    if 0xBDF1 <= num <= 0xBE0B:
        return "LVT"
    if 0xBE0D <= num <= 0xBE27:
        return "LVT"
    if 0xBE29 <= num <= 0xBE43:
        return "LVT"
    if 0xBE45 <= num <= 0xBE5F:
        return "LVT"
    if 0xBE61 <= num <= 0xBE7B:
        return "LVT"
    if 0xBE7D <= num <= 0xBE97:
        return "LVT"
    if 0xBE99 <= num <= 0xBEB3:
        return "LVT"
    if 0xBEB5 <= num <= 0xBECF:
        return "LVT"
    if 0xBED1 <= num <= 0xBEEB:
        return "LVT"
    if 0xBEED <= num <= 0xBF07:
        return "LVT"
    if 0xBF09 <= num <= 0xBF23:
        return "LVT"
    if 0xBF25 <= num <= 0xBF3F:
        return "LVT"
    if 0xBF41 <= num <= 0xBF5B:
        return "LVT"
    if 0xBF5D <= num <= 0xBF77:
        return "LVT"
    if 0xBF79 <= num <= 0xBF93:
        return "LVT"
    if 0xBF95 <= num <= 0xBFAF:
        return "LVT"
    if 0xBFB1 <= num <= 0xBFCB:
        return "LVT"
    if 0xBFCD <= num <= 0xBFE7:
        return "LVT"
    if 0xBFE9 <= num <= 0xC003:
        return "LVT"
    if 0xC005 <= num <= 0xC01F:
        return "LVT"
    if 0xC021 <= num <= 0xC03B:
        return "LVT"
    if 0xC03D <= num <= 0xC057:
        return "LVT"
    if 0xC059 <= num <= 0xC073:
        return "LVT"
    if 0xC075 <= num <= 0xC08F:
        return "LVT"
    if 0xC091 <= num <= 0xC0AB:
        return "LVT"
    if 0xC0AD <= num <= 0xC0C7:
        return "LVT"
    if 0xC0C9 <= num <= 0xC0E3:
        return "LVT"
    if 0xC0E5 <= num <= 0xC0FF:
        return "LVT"
    if 0xC101 <= num <= 0xC11B:
        return "LVT"
    if 0xC11D <= num <= 0xC137:
        return "LVT"
    if 0xC139 <= num <= 0xC153:
        return "LVT"
    if 0xC155 <= num <= 0xC16F:
        return "LVT"
    if 0xC171 <= num <= 0xC18B:
        return "LVT"
    if 0xC18D <= num <= 0xC1A7:
        return "LVT"
    if 0xC1A9 <= num <= 0xC1C3:
        return "LVT"
    if 0xC1C5 <= num <= 0xC1DF:
        return "LVT"
    if 0xC1E1 <= num <= 0xC1FB:
        return "LVT"
    if 0xC1FD <= num <= 0xC217:
        return "LVT"
    if 0xC219 <= num <= 0xC233:
        return "LVT"
    if 0xC235 <= num <= 0xC24F:
        return "LVT"
    if 0xC251 <= num <= 0xC26B:
        return "LVT"
    if 0xC26D <= num <= 0xC287:
        return "LVT"
    if 0xC289 <= num <= 0xC2A3:
        return "LVT"
    if 0xC2A5 <= num <= 0xC2BF:
        return "LVT"
    if 0xC2C1 <= num <= 0xC2DB:
        return "LVT"
    if 0xC2DD <= num <= 0xC2F7:
        return "LVT"
    if 0xC2F9 <= num <= 0xC313:
        return "LVT"
    if 0xC315 <= num <= 0xC32F:
        return "LVT"
    if 0xC331 <= num <= 0xC34B:
        return "LVT"
    if 0xC34D <= num <= 0xC367:
        return "LVT"
    if 0xC369 <= num <= 0xC383:
        return "LVT"
    if 0xC385 <= num <= 0xC39F:
        return "LVT"
    if 0xC3A1 <= num <= 0xC3BB:
        return "LVT"
    if 0xC3BD <= num <= 0xC3D7:
        return "LVT"
    if 0xC3D9 <= num <= 0xC3F3:
        return "LVT"
    if 0xC3F5 <= num <= 0xC40F:
        return "LVT"
    if 0xC411 <= num <= 0xC42B:
        return "LVT"
    if 0xC42D <= num <= 0xC447:
        return "LVT"
    if 0xC449 <= num <= 0xC463:
        return "LVT"
    if 0xC465 <= num <= 0xC47F:
        return "LVT"
    if 0xC481 <= num <= 0xC49B:
        return "LVT"
    if 0xC49D <= num <= 0xC4B7:
        return "LVT"
    if 0xC4B9 <= num <= 0xC4D3:
        return "LVT"
    if 0xC4D5 <= num <= 0xC4EF:
        return "LVT"
    if 0xC4F1 <= num <= 0xC50B:
        return "LVT"
    if 0xC50D <= num <= 0xC527:
        return "LVT"
    if 0xC529 <= num <= 0xC543:
        return "LVT"
    if 0xC545 <= num <= 0xC55F:
        return "LVT"
    if 0xC561 <= num <= 0xC57B:
        return "LVT"
    if 0xC57D <= num <= 0xC597:
        return "LVT"
    if 0xC599 <= num <= 0xC5B3:
        return "LVT"
    if 0xC5B5 <= num <= 0xC5CF:
        return "LVT"
    if 0xC5D1 <= num <= 0xC5EB:
        return "LVT"
    if 0xC5ED <= num <= 0xC607:
        return "LVT"
    if 0xC609 <= num <= 0xC623:
        return "LVT"
    if 0xC625 <= num <= 0xC63F:
        return "LVT"
    if 0xC641 <= num <= 0xC65B:
        return "LVT"
    if 0xC65D <= num <= 0xC677:
        return "LVT"
    if 0xC679 <= num <= 0xC693:
        return "LVT"
    if 0xC695 <= num <= 0xC6AF:
        return "LVT"
    if 0xC6B1 <= num <= 0xC6CB:
        return "LVT"
    if 0xC6CD <= num <= 0xC6E7:
        return "LVT"
    if 0xC6E9 <= num <= 0xC703:
        return "LVT"
    if 0xC705 <= num <= 0xC71F:
        return "LVT"
    if 0xC721 <= num <= 0xC73B:
        return "LVT"
    if 0xC73D <= num <= 0xC757:
        return "LVT"
    if 0xC759 <= num <= 0xC773:
        return "LVT"
    if 0xC775 <= num <= 0xC78F:
        return "LVT"
    if 0xC791 <= num <= 0xC7AB:
        return "LVT"
    if 0xC7AD <= num <= 0xC7C7:
        return "LVT"
    if 0xC7C9 <= num <= 0xC7E3:
        return "LVT"
    if 0xC7E5 <= num <= 0xC7FF:
        return "LVT"
    if 0xC801 <= num <= 0xC81B:
        return "LVT"
    if 0xC81D <= num <= 0xC837:
        return "LVT"
    if 0xC839 <= num <= 0xC853:
        return "LVT"
    if 0xC855 <= num <= 0xC86F:
        return "LVT"
    if 0xC871 <= num <= 0xC88B:
        return "LVT"
    if 0xC88D <= num <= 0xC8A7:
        return "LVT"
    if 0xC8A9 <= num <= 0xC8C3:
        return "LVT"
    if 0xC8C5 <= num <= 0xC8DF:
        return "LVT"
    if 0xC8E1 <= num <= 0xC8FB:
        return "LVT"
    if 0xC8FD <= num <= 0xC917:
        return "LVT"
    if 0xC919 <= num <= 0xC933:
        return "LVT"
    if 0xC935 <= num <= 0xC94F:
        return "LVT"
    if 0xC951 <= num <= 0xC96B:
        return "LVT"
    if 0xC96D <= num <= 0xC987:
        return "LVT"
    if 0xC989 <= num <= 0xC9A3:
        return "LVT"
    if 0xC9A5 <= num <= 0xC9BF:
        return "LVT"
    if 0xC9C1 <= num <= 0xC9DB:
        return "LVT"
    if 0xC9DD <= num <= 0xC9F7:
        return "LVT"
    if 0xC9F9 <= num <= 0xCA13:
        return "LVT"
    if 0xCA15 <= num <= 0xCA2F:
        return "LVT"
    if 0xCA31 <= num <= 0xCA4B:
        return "LVT"
    if 0xCA4D <= num <= 0xCA67:
        return "LVT"
    if 0xCA69 <= num <= 0xCA83:
        return "LVT"
    if 0xCA85 <= num <= 0xCA9F:
        return "LVT"
    if 0xCAA1 <= num <= 0xCABB:
        return "LVT"
    if 0xCABD <= num <= 0xCAD7:
        return "LVT"
    if 0xCAD9 <= num <= 0xCAF3:
        return "LVT"
    if 0xCAF5 <= num <= 0xCB0F:
        return "LVT"
    if 0xCB11 <= num <= 0xCB2B:
        return "LVT"
    if 0xCB2D <= num <= 0xCB47:
        return "LVT"
    if 0xCB49 <= num <= 0xCB63:
        return "LVT"
    if 0xCB65 <= num <= 0xCB7F:
        return "LVT"
    if 0xCB81 <= num <= 0xCB9B:
        return "LVT"
    if 0xCB9D <= num <= 0xCBB7:
        return "LVT"
    if 0xCBB9 <= num <= 0xCBD3:
        return "LVT"
    if 0xCBD5 <= num <= 0xCBEF:
        return "LVT"
    if 0xCBF1 <= num <= 0xCC0B:
        return "LVT"
    if 0xCC0D <= num <= 0xCC27:
        return "LVT"
    if 0xCC29 <= num <= 0xCC43:
        return "LVT"
    if 0xCC45 <= num <= 0xCC5F:
        return "LVT"
    if 0xCC61 <= num <= 0xCC7B:
        return "LVT"
    if 0xCC7D <= num <= 0xCC97:
        return "LVT"
    if 0xCC99 <= num <= 0xCCB3:
        return "LVT"
    if 0xCCB5 <= num <= 0xCCCF:
        return "LVT"
    if 0xCCD1 <= num <= 0xCCEB:
        return "LVT"
    if 0xCCED <= num <= 0xCD07:
        return "LVT"
    if 0xCD09 <= num <= 0xCD23:
        return "LVT"
    if 0xCD25 <= num <= 0xCD3F:
        return "LVT"
    if 0xCD41 <= num <= 0xCD5B:
        return "LVT"
    if 0xCD5D <= num <= 0xCD77:
        return "LVT"
    if 0xCD79 <= num <= 0xCD93:
        return "LVT"
    if 0xCD95 <= num <= 0xCDAF:
        return "LVT"
    if 0xCDB1 <= num <= 0xCDCB:
        return "LVT"
    if 0xCDCD <= num <= 0xCDE7:
        return "LVT"
    if 0xCDE9 <= num <= 0xCE03:
        return "LVT"
    if 0xCE05 <= num <= 0xCE1F:
        return "LVT"
    if 0xCE21 <= num <= 0xCE3B:
        return "LVT"
    if 0xCE3D <= num <= 0xCE57:
        return "LVT"
    if 0xCE59 <= num <= 0xCE73:
        return "LVT"
    if 0xCE75 <= num <= 0xCE8F:
        return "LVT"
    if 0xCE91 <= num <= 0xCEAB:
        return "LVT"
    if 0xCEAD <= num <= 0xCEC7:
        return "LVT"
    if 0xCEC9 <= num <= 0xCEE3:
        return "LVT"
    if 0xCEE5 <= num <= 0xCEFF:
        return "LVT"
    if 0xCF01 <= num <= 0xCF1B:
        return "LVT"
    if 0xCF1D <= num <= 0xCF37:
        return "LVT"
    if 0xCF39 <= num <= 0xCF53:
        return "LVT"
    if 0xCF55 <= num <= 0xCF6F:
        return "LVT"
    if 0xCF71 <= num <= 0xCF8B:
        return "LVT"
    if 0xCF8D <= num <= 0xCFA7:
        return "LVT"
    if 0xCFA9 <= num <= 0xCFC3:
        return "LVT"
    if 0xCFC5 <= num <= 0xCFDF:
        return "LVT"
    if 0xCFE1 <= num <= 0xCFFB:
        return "LVT"
    if 0xCFFD <= num <= 0xD017:
        return "LVT"
    if 0xD019 <= num <= 0xD033:
        return "LVT"
    if 0xD035 <= num <= 0xD04F:
        return "LVT"
    if 0xD051 <= num <= 0xD06B:
        return "LVT"
    if 0xD06D <= num <= 0xD087:
        return "LVT"
    if 0xD089 <= num <= 0xD0A3:
        return "LVT"
    if 0xD0A5 <= num <= 0xD0BF:
        return "LVT"
    if 0xD0C1 <= num <= 0xD0DB:
        return "LVT"
    if 0xD0DD <= num <= 0xD0F7:
        return "LVT"
    if 0xD0F9 <= num <= 0xD113:
        return "LVT"
    if 0xD115 <= num <= 0xD12F:
        return "LVT"
    if 0xD131 <= num <= 0xD14B:
        return "LVT"
    if 0xD14D <= num <= 0xD167:
        return "LVT"
    if 0xD169 <= num <= 0xD183:
        return "LVT"
    if 0xD185 <= num <= 0xD19F:
        return "LVT"
    if 0xD1A1 <= num <= 0xD1BB:
        return "LVT"
    if 0xD1BD <= num <= 0xD1D7:
        return "LVT"
    if 0xD1D9 <= num <= 0xD1F3:
        return "LVT"
    if 0xD1F5 <= num <= 0xD20F:
        return "LVT"
    if 0xD211 <= num <= 0xD22B:
        return "LVT"
    if 0xD22D <= num <= 0xD247:
        return "LVT"
    if 0xD249 <= num <= 0xD263:
        return "LVT"
    if 0xD265 <= num <= 0xD27F:
        return "LVT"
    if 0xD281 <= num <= 0xD29B:
        return "LVT"
    if 0xD29D <= num <= 0xD2B7:
        return "LVT"
    if 0xD2B9 <= num <= 0xD2D3:
        return "LVT"
    if 0xD2D5 <= num <= 0xD2EF:
        return "LVT"
    if 0xD2F1 <= num <= 0xD30B:
        return "LVT"
    if 0xD30D <= num <= 0xD327:
        return "LVT"
    if 0xD329 <= num <= 0xD343:
        return "LVT"
    if 0xD345 <= num <= 0xD35F:
        return "LVT"
    if 0xD361 <= num <= 0xD37B:
        return "LVT"
    if 0xD37D <= num <= 0xD397:
        return "LVT"
    if 0xD399 <= num <= 0xD3B3:
        return "LVT"
    if 0xD3B5 <= num <= 0xD3CF:
        return "LVT"
    if 0xD3D1 <= num <= 0xD3EB:
        return "LVT"
    if 0xD3ED <= num <= 0xD407:
        return "LVT"
    if 0xD409 <= num <= 0xD423:
        return "LVT"
    if 0xD425 <= num <= 0xD43F:
        return "LVT"
    if 0xD441 <= num <= 0xD45B:
        return "LVT"
    if 0xD45D <= num <= 0xD477:
        return "LVT"
    if 0xD479 <= num <= 0xD493:
        return "LVT"
    if 0xD495 <= num <= 0xD4AF:
        return "LVT"
    if 0xD4B1 <= num <= 0xD4CB:
        return "LVT"
    if 0xD4CD <= num <= 0xD4E7:
        return "LVT"
    if 0xD4E9 <= num <= 0xD503:
        return "LVT"
    if 0xD505 <= num <= 0xD51F:
        return "LVT"
    if 0xD521 <= num <= 0xD53B:
        return "LVT"
    if 0xD53D <= num <= 0xD557:
        return "LVT"
    if 0xD559 <= num <= 0xD573:
        return "LVT"
    if 0xD575 <= num <= 0xD58F:
        return "LVT"
    if 0xD591 <= num <= 0xD5AB:
        return "LVT"
    if 0xD5AD <= num <= 0xD5C7:
        return "LVT"
    if 0xD5C9 <= num <= 0xD5E3:
        return "LVT"
    if 0xD5E5 <= num <= 0xD5FF:
        return "LVT"
    if 0xD601 <= num <= 0xD61B:
        return "LVT"
    if 0xD61D <= num <= 0xD637:
        return "LVT"
    if 0xD639 <= num <= 0xD653:
        return "LVT"
    if 0xD655 <= num <= 0xD66F:
        return "LVT"
    if 0xD671 <= num <= 0xD68B:
        return "LVT"
    if 0xD68D <= num <= 0xD6A7:
        return "LVT"
    if 0xD6A9 <= num <= 0xD6C3:
        return "LVT"
    if 0xD6C5 <= num <= 0xD6DF:
        return "LVT"
    if 0xD6E1 <= num <= 0xD6FB:
        return "LVT"
    if 0xD6FD <= num <= 0xD717:
        return "LVT"
    if 0xD719 <= num <= 0xD733:
        return "LVT"
    if 0xD735 <= num <= 0xD74F:
        return "LVT"
    if 0xD751 <= num <= 0xD76B:
        return "LVT"
    if 0xD76D <= num <= 0xD787:
        return "LVT"
    if 0xD789 <= num <= 0xD7A3:
        return "LVT"
    return "Other"
