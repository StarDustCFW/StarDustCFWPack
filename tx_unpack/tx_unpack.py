###############################################
# TX SX OS unpacker - by hexkyz and naehrwert #
###############################################

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import struct

"""
typedef struct boot_dat_hdr
{
    unsigned char ident[0x10];
    unsigned char sha2_s2[0x20];
    unsigned int s2_dst;
    unsigned int s2_size;
    unsigned int s2_enc;
    unsigned char pad[0x10];
    unsigned int s3_size;
    unsigned char pad2[0x90];
    unsigned char sha2_hdr[0x20];
} boot_dat_hdr_t;
"""

def aes_ctr_dec(buf, key, iv):
    ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))
    return AES.new(key, AES.MODE_CTR, counter=ctr).encrypt(buf)

f = open("boot.dat", "rb")
b = f.read()
f.close()

boot_ver = struct.unpack("II", b[0x08:0x10])
s2_base, s2_size = struct.unpack("II", b[0x30:0x38])
s2_key = "47E6BFB05965ABCD00E2EE4DDF540261".decode("hex")
s2_ctr = "8E4C7889CBAE4A3D64797DDA84BDB086".decode("hex")

if boot_ver[1] == 0x302E3156:      # TX BOOT V1.0
    arm64_key = "35D8FFC4AA1BAB9514825EB0658FB493".decode("hex")
    arm64_ctr = "C38EA26FF3CCE98FD8D5ED431D9D5B94".decode("hex")
    arm64_off = 0x53BAB0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
    
    fb_key = "E2AC05206A701C9AA514D2B2B7C9F395".decode("hex")
    fb_ctr = "46FAB59AF0E469EF116614DEC366D15F".decode("hex")
    fb_off = 0x17BAB0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload80_key = "030D865B7E458B10AD5706F6E227F4EB".decode("hex")
    payload80_ctr = "AFFC93692EBD2E3D252339F01E03416B".decode("hex")
    payload80_off = 0x5F40
    payload80_size = 0x175B70
    payload80_base = 0x80000000
elif boot_ver[1] == 0x312E3156:    # TX BOOT V1.1
    arm64_key = "51A39F0B46BAE4691AD39A698146E865".decode("hex")
    arm64_ctr = "7A307ED7F1ECC792F0E821ECD6999853".decode("hex")
    arm64_off = 0x53BAE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
    
    fb_key = "27BABEE3DCFEF100C744A2388B57E957".decode("hex")
    fb_ctr = "0B88AC25AFAF9B92D81372331AD66E24".decode("hex")
    fb_off = 0x17BAE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload80_key = "8D6FEABE0F3936145A474D3F05D33679".decode("hex")
    payload80_ctr = "2846EFA9DACB065C51C71C154F0E9EA2".decode("hex")
    payload80_off = 0x5F50
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x322E3156:    # TX BOOT V1.2
    arm64_key = "22429923901AF74ED6944992C824ACFE".decode("hex")
    arm64_ctr = "590BE04550CC6139921D1C95241F34AC".decode("hex")
    arm64_off = 0x53BAD0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "E483A884AB59D5D0014404C2EB698517".decode("hex")
    fb_ctr = "55A60F59F29DD518B4CAA59D0E3D1629".decode("hex")
    fb_off = 0x17BAD0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "AF8F5811D075F5317924E5C1DD70A531".decode("hex")
    payload80_ctr = "78219A2BB518BF9E302AFF75CE5862E1".decode("hex")
    payload80_off = 0x5F50
    payload80_size = 0x175B80
    payload80_base = 0x80000000
elif boot_ver[1] == 0x332E3156:    # TX BOOT V1.3
    arm64_key = "0DA0D677361625E81FD6DF236B9450D5".decode("hex")
    arm64_ctr = "B368ECA0F8C078908F6B979613D0E52A".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "1E76718F0BAF7D8BB72ECCE4F657DAF8".decode("hex")
    fb_ctr = "4B0D81D9F44B8458F1EA93324C40BCD1".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "5B52BF7DED400C967FB0B2E013B55E68".decode("hex")
    payload80_ctr = "A1E038CE082F2C26052BE75F111CE3D1".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x342E3156:    # TX BOOT V1.4
    arm64_key = "C1BAE9D0BDBC2CFFE702BB071E5F08DD".decode("hex")
    arm64_ctr = "030B4E269E13F89A13D25F45474FB3C7".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "01009C5028E64261ABA99BDD588D062A".decode("hex")
    fb_ctr = "ED2FD755767BC51052B2414F938AA960".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "9BF5F63498B8CB415D33F78CAA18CBE8".decode("hex")
    payload80_ctr = "0886AA9881287E4D0529F011D6ED8DE2".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x352E3156:    # TX BOOT V1.5
    arm64_key = "407CC1C82F9C2E527C4A1B2EB37B323D".decode("hex")
    arm64_ctr = "92C67922E69AFFB196D9B69E7B2127C8".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "99A5466D889C26E1E7D0B22DF4684264".decode("hex")
    fb_ctr = "8649C0C70C461E4AB4A0299547655EF6".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "F98AF4F9797B7817BD9815D7B238D077".decode("hex")
    payload80_ctr = "A4D4D0F8A7946F2AD2E479CCDD3F5A9F".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x362E3156:    # TX BOOT V1.6
    arm64_key = "81A2CEBC2923A84082A2738B62AE4237".decode("hex")
    arm64_ctr = "B5EB1DEC39C6D6D75EFBAD01215CF01B".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "345F7D4471FB2B21CA5CCFE4C6432959".decode("hex")
    fb_ctr = "B488803EA9C1EBCEFEFF6A3F9D813BB2".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "06BA3CE40A34917CD5791F5AA07C5678".decode("hex")
    payload80_ctr = "938AF18A64DB9899921B896BF8F9F190".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x372E3156:    # TX BOOT V1.7
    arm64_key = "469481EDF8300C6F02A860479AEDEE70".decode("hex")
    arm64_ctr = "E68E3300AB7837501D20D53218363937".decode("hex")
    arm64_off = 0x53BB70
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "D61B4F92411613F1EF352446C898A1BA".decode("hex")
    fb_ctr = "CC4BB77C97C741E54C2BDB02B797A1D4".decode("hex")
    fb_off = 0x17BB70
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "F6319F3E4C4D6DDC11154B50DBD80AF2".decode("hex")
    payload80_ctr = "429DF9227D66937F1F80F3F0E57B24E8".decode("hex")
    payload80_off = 0x5FE0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x382E3156:    # TX BOOT V1.8
    arm64_key = "080B73616C9E082B934F31F6C5B112FD".decode("hex")
    arm64_ctr = "8F13149E9F88FE285D375E856CEA4C80".decode("hex")
    arm64_off = 0x53BB70
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "5358EB25799A7DB78539DF6170F7E48F".decode("hex")
    fb_ctr = "3B3616F6375038D975E71E488A34CE7F".decode("hex")
    fb_off = 0x17BB70
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "3CA900F5767B81D0F9294E1C6EA6E972".decode("hex")
    payload80_ctr = "508E7E6941A9021F4BC1D85BF081F6C8".decode("hex")
    payload80_off = 0x5FE0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x392E3156:    # TX BOOT V1.9
    arm64_key = "8FF020361DC5EE595B24432190A56A37".decode("hex")
    arm64_ctr = "9601BB4E5D8B96505BD8600636A6B6F6".decode("hex")
    arm64_off = 0x53F7B0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "D00D6F8135CAC6D48A5F5E538953F194".decode("hex")
    fb_ctr = "AF73E22FE3B4120E8AD00411F9B507EE".decode("hex")
    fb_off = 0x17F7B0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "88D11A7F1DA0744E24D5080CC6E60144".decode("hex")
    payload80_ctr = "A530383538AB4E14BB593CC63056FC31".decode("hex")
    payload80_off = 0x9C20
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif boot_ver[1] == 0x302E3256:    # TX BOOT V2.0
    arm64_key = "5421346FCE84BB6AEC3AEF846DF1F827".decode("hex")
    arm64_ctr = "48ADCB7E1696EDEB0A3D5BEE6A131DCB".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "5F58D9832339AC0B1B7893573575E77E".decode("hex")
    fb_ctr = "05BE5152A45F3E47BA9941E6FED1D166".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "1A4B9803CB5CF96B7F17167A558A77F8".decode("hex")
    payload80_ctr = "EDDDC820771DBAA60A16CC2CCB1AE5D8".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x302E3256):    # TX BOOT V2.0.1
    arm64_key = "88F63BD5167EC20830152F043E689EB8".decode("hex")
    arm64_ctr = "B0DA5DC62EB6F5B5AE2CBD4E76B3E243".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "1FBC61D0C68485EE7E0CCEFDA071455F".decode("hex")
    fb_ctr = "AC5525DB506255FA65F5FB4861347725".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "C9B2B700D354E3C2B4A7B1E0B3391B28".decode("hex")
    payload80_ctr = "AE809C9199F025B3A511ABC778B9BFDD".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x312E3256):        # TX BOOT V2.1
    arm64_key = "726D57B05F0B2BC6F6A31E7ADF21618E".decode("hex")
    arm64_ctr = "6FBF960EDBC5EA149FCC7675439B2368".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "518F2FFC9B4AEC2BF5A488B439366408".decode("hex")
    fb_ctr = "46689C134D45E2FD7639220FB8FAB472".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0ADF1975F209A3B093B60A3FF32EE146".decode("hex")
    payload80_ctr = "CDCAA8CEAA893BC6B2B4C8F44CF11970".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x322E3256):        # TX BOOT V2.2
    arm64_key = "912F24E1F53D56CA9805D14BDBF8A0D1".decode("hex")
    arm64_ctr = "D6DA10E22727B429527D511DAF0243F5".decode("hex")
    arm64_off = 0x5400B0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "9FECE0235086D7DF3ED4EFC7FCFA63F7".decode("hex")
    fb_ctr = "76CA419A93A544988C96BA8828B46E92".decode("hex")
    fb_off = 0x1800B0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "B98F301D97A66F3EF3ADE65E8E78014A".decode("hex")
    payload80_ctr = "3448F56D78DBD16CD8D1D9E28D3349E8".decode("hex")
    payload80_off = 0xA520
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x322E3256):    # TX BOOT V2.2.1
    arm64_key = "DF7F3184C466FAA56EDFCC43E74905A0".decode("hex")
    arm64_ctr = "4B6DB003373192CABA447B5E3305D779".decode("hex")
    arm64_off = 0x540530
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "72CB3A30DED6AC9C8DDDDCE778AF18C3".decode("hex")
    fb_ctr = "0DCF05FCD3165ED2B76E9E5048EA5FE0".decode("hex")
    fb_off = 0x180530
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0CE4F9BE6BCE9D4FC85CF56110D03F15".decode("hex")
    payload80_ctr = "F60A799057A5ABE69D56E40089DDEDF7".decode("hex")
    payload80_off = 0xA9A0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x332E3256):    # TX BOOT V2.3
    arm64_key = "CF7286C1F8C3300F9E9F218065CE6FE0".decode("hex")
    arm64_ctr = "9B285AD4E527E3ADDDCBFDA21536E2D0".decode("hex")
    arm64_off = 0x540650
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "3842A6270DF9488EF47D7FD28106502E".decode("hex")
    fb_ctr = "AF95C4B76752D5360CEE8DA3613E5ACD".decode("hex")
    fb_off = 0x180650
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0C482DA896C0F1A20785D773E541D5C4".decode("hex")
    payload80_ctr = "C6A03A8ACE0C553F43D36EF71679232F".decode("hex")
    payload80_off = 0xAAD0
    payload80_size = 0x175B80
    payload80_base = 0x80000000
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x342E3256):    # TX BOOT V2.4
    arm64_key = "E2E56C54A36A9F0E91249B01E522ED1E".decode("hex")
    arm64_ctr = "B54A8A7BBD65DEA725E5FB6CBC19BC77".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "4F5E892DDA5946254E33C2F7D76B7904".decode("hex")
    fb_ctr = "2965E52C440D0A90861D18A9F09518D2".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "3CDC53A1FA0725B0A0FBEA7A47A711D2".decode("hex")
    payload80_ctr = "5BB2774E4BB8D05C6A6A707BE87792B6".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x342E3256):    # TX BOOT V2.4.1
    arm64_key = "AD52C9AC41A930629A1C007832EA656C".decode("hex")
    arm64_ctr = "3DB839FD3C3AC1718D2AEFCD474FC510".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "393046399B2CE12109B7E250EB7E66B8".decode("hex")
    fb_ctr = "1CABBB1A1E2C18ECA2C623EAEFF10DC3".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "80261C64FB62543607DE3179FDB8BD8F".decode("hex")
    payload80_ctr = "0997749F304867A249FE5154CAE19114".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5
    arm64_key = "DBD3059B920D1CC75C555401CDEC045E".decode("hex")
    arm64_ctr = "69C7E7E3E2ACD315E74C6040386108A6".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "F087C3E9E75674DA01D0CFAF44279B6D".decode("hex")
    fb_ctr = "5544128B01DA21DC065536A7D29A795C".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "FA50BBB9499D3F790D733633BDF4D9DB".decode("hex")
    payload80_ctr = "A4C2D2ED364D57412C2384CDA65C3434".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.1
    arm64_key = "B6F78BEB41AB6982B0916C09749E3538".decode("hex")
    arm64_ctr = "3ECA0C1E11AC66E9D9BE36E8C69F1675".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "3AD0173DC807EEF2A10106A02423F36F".decode("hex")
    fb_ctr = "55EE810C8B37616E88FD60E8A88C4484".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "E58C28B94260E1C68DC83A15199AB43E".decode("hex")
    payload80_ctr = "34A5A9BE720951098473FF91FAE4AB0D".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.2
    arm64_key = "0883194678432CD79ED54ED7C5D1CBEC".decode("hex")
    arm64_ctr = "72D199289598A3DCD84C06ECDFA85DDE".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "14C3A3A33B4B1F4659F364DC29422DFD".decode("hex")
    fb_ctr = "2ADA0FD01AB8CEC1669BB97E616E1CBD".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "172A09354DA46832FDCC89E8511898DF".decode("hex")
    payload80_ctr = "40AE331DEF273A6E76FB803AD7460167".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
elif (boot_ver[1] == 0x332E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.3
    arm64_key = "5C1D2D863D75E399E79BE6A7F8298FD4".decode("hex")
    arm64_ctr = "2ECEECE30C6C98EB47F2519381178CF2".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "700C5C4A5A8A4930577E6712B7B0BF42".decode("hex")
    fb_ctr = "E6B5B163DE91E6A04F5E7E7DCD44DD84".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "992DCFF93D1346957F57116D5FF0E902".decode("hex")
    payload80_ctr = "A446E7629E99B02C6F2770D99B877E62".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
else:
    exit()

# Create main folder
if not os.path.exists("./sxos/"):
    os.mkdir("./sxos/")
os.chdir("./sxos/")

# Create folder for the initial boot files
if not os.path.exists("./init/"):
    os.mkdir("./init/")
os.chdir("./init/")
    
# Decrypt Stage2 IRAM payload
f = open("stage2_{0:08X}.bin".format(s2_base), "wb")
f.write(aes_ctr_dec(b[0x100:0x100+s2_size], s2_key, s2_ctr))
f.close()

# Decrypt ARM64 memory training blob
f = open("arm64_{0:08X}.bin".format(arm64_base), "wb")
f.write(aes_ctr_dec(b[arm64_off:arm64_off+arm64_size], arm64_key, arm64_ctr))
f.close()

# Decrypt initial framebuffer binary
f = open("fb_{0:08X}.bin".format(fb_base), "wb")
f.write(aes_ctr_dec(b[fb_off:fb_off+fb_size], fb_key, fb_ctr))
f.close()

# Create folder for the obfuscation payloads
if not os.path.exists("../payloads/"):
    os.mkdir("../payloads/")
os.chdir("../payloads/")

# Decrypt first layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payload80_base), "wb")
f.write(aes_ctr_dec(b[payload80_off:payload80_off+payload80_size], payload80_key, payload80_ctr))
f.close()

if boot_ver[1] == 0x302E3156:      # TX BOOT V1.0
    payload90_key = "7F5ADF4D874E452E03D49127A42F1E76".decode("hex")
    payload90_ctr = "94251152C910E701397BE2DB4F1C6CA8".decode("hex")
    payload90_off = 0xC0B8D0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "7D3903433AFF4454E7C4494CF78B2C27".decode("hex")
    payload98_ctr = "47A6B1EE20DDB7CDBB4A486C42638D54".decode("hex")
    payload98_off = 0xD013F0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "470248AF0FD18221C7920635705980F6".decode("hex")
    payloadA0_ctr = "4CC30D28126D38749F755A506B21EE15".decode("hex")
    payloadA0_off = 0xDBD680
    payloadA0_size = 0x1154D0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C9B5A5746CF37F46417DD6842B48361B".decode("hex")
    bootloader_ctr = "40FBE01C573B0C286BC7956455475788".decode("hex")
    bootloader_off = 0x571E20
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "677EC85A86F798AFD6B8BC046B65F0F5".decode("hex")
    assets_ctr = "31C8DBE98486D59CD69DA7C470A69A0B".decode("hex")
    assets_off = 0x592DE0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "31756DA6C12CA907C050861D60A5E0A5".decode("hex")
    fw_ctr = "DA0F8243F83358F15F431FF6F674C099".decode("hex")
    fw_off = 0
    fw_size = 0x1154D0
elif boot_ver[1] == 0x312E3156:      # TX BOOT V1.1
    payload90_key = "7013D0DDA6F8C9149163EA51A67018B1".decode("hex")
    payload90_ctr = "E3D4923757E97D29CFAD58896D53EE85".decode("hex")
    payload90_off = 0xC0B900
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "28E56A613F36B70FE295E22A44DA918E".decode("hex")
    payload98_ctr = "82566B8311E419CD238F9454994A6904".decode("hex")
    payload98_off = 0xD01420
    payload98_size = 0xBC290
    payload98_base = 0x98000000

    payloadA0_key = "7A0E46F3E362CCBC9988171F9EA89F47".decode("hex")
    payloadA0_ctr = "8074330C69CA88D593EFF15670E78989".decode("hex")
    payloadA0_off = 0xDBD6B0
    payloadA0_size = 0x115870
    payloadA0_base = 0xA0000000
    
    bootloader_key = "9C333852BBABC82FE5AD8C8D7EC05BF7".decode("hex")
    bootloader_ctr = "7214E2B09A5C7B9DC54FDB8C46CFFD59".decode("hex")
    bootloader_off = 0x571E50
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "B9501029CBB75F277EE8315F26DD4BCE".decode("hex")
    assets_ctr = "6C99263F2A07EFBA2A5A9609F02746BB".decode("hex")
    assets_off = 0x592E10
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "78176C951176AE5B0B6784F45B8553FC".decode("hex")
    fw_ctr = "56B409BC21DB9A7FEC8ED64C5A7E09D0".decode("hex")
    fw_off = 0
    fw_size = 0x115870
elif boot_ver[1] == 0x322E3156:      # TX BOOT V1.2
    payload90_key = "3DE87D8E1A24E06B2D50F6100AA09B4C".decode("hex")
    payload90_ctr = "94162463FF6B54FE9B6683F72CE79760".decode("hex")
    payload90_off = 0xC0B8F0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "5EBBF535CA7C7EE6C97A770CB1AA7E37".decode("hex")
    payload98_ctr = "BF9BA9CB3E2328ACD4676CE106081B3D".decode("hex")
    payload98_off = 0xD01410
    payload98_size = 0xBC290
    payload98_base = 0x98000000

    payloadA0_key = "9EBBBD4F4A5CC82B705431DFF5AA260A".decode("hex")
    payloadA0_ctr = "8A7923E459F12ED38CD533EFF69727D9".decode("hex")
    payloadA0_off = 0xDBD6A0
    payloadA0_size = 0x120530
    payloadA0_base = 0xA0000000
    
    bootloader_key = "F1A4E1EE2F279BB55A0C16D0373961BC".decode("hex")
    bootloader_ctr = "BC40537AB5F23088B9F1DD51FB0BB1D7".decode("hex")
    bootloader_off = 0x571E40
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "8D0CC65A2DE679BDB3D73C3F11734E0E".decode("hex")
    assets_ctr = "6CA93EAEEC84E218918F68DBFF8C95E9".decode("hex")
    assets_off = 0x592E00
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "84BB031A9E20D2BEAA10CE85BD4157BF".decode("hex")
    fw_ctr = "DC986E7B0FF4DD433F21D655B082BF43".decode("hex")
    fw_off = 0
    fw_size = 0x120530
elif boot_ver[1] == 0x332E3156:      # TX BOOT V1.3
    payload90_key = "36FC59BEBA2AABC77D124668E025350E".decode("hex")
    payload90_ctr = "E773714BD860B532A356F2C6A07B843E".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "9334A1F1943C16B2506BB1D9EBF33F93".decode("hex")
    payload98_ctr = "7BE8A72FBA0943AE57E93E6F6D6FB46A".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F1AC8CB71383F07FAF34C12879025BEE".decode("hex")
    payloadA0_ctr = "86B9D01C6FFAAF157CE31AE1162A7C48".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x1312E0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C439958095F3AC5CA361E46481A778B4".decode("hex")
    bootloader_ctr = "07E32283C45EC5215DEFDBB199AD2F5B".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "5E5C65FA5C93C43BD8BA5B7B93A59687".decode("hex")
    assets_ctr = "45E156D62914D27529AA7A8B7EAC8A31".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "264AAE11C24A65AB99E021788BFE6E66".decode("hex")
    fw_ctr = "71C68F4C9CBB2203AC267B917BAC76B0".decode("hex")
    fw_off = 0
    fw_size = 0x1312E0
elif boot_ver[1] == 0x342E3156:      # TX BOOT V1.4
    payload90_key = "404C0187E5B990DCED5180D1F8A6041B".decode("hex")
    payload90_ctr = "ADAD0B390E3192F7A8BB969C1F0F0485".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "E84E13FFD5C88C1B5C517E9DDB3EDAF9".decode("hex")
    payload98_ctr = "DBFCDD08231C6232029021EFDBDDC960".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "2C4E4F4389D142C5C8F19E221852241E".decode("hex")
    payloadA0_ctr = "CA9CCD03146F35CA1BEF06C8D3B37E2B".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x59FF0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FADE622772177CC77B145F98A4D929BF".decode("hex")
    bootloader_ctr = "28EC8A0780FCDDD588467DD5143D8615".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "6F7FCB8B647E3B8F571B1897C9C87436".decode("hex")
    assets_ctr = "B43F32C904EDF459BC4811A6E074D86F".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "B8C11D378EE722BA3402B669C7278879".decode("hex")
    fw_ctr = "8FF8C494DED46749215202407DB70357".decode("hex")
    fw_off = 0
    fw_size = 0x59FF0
elif boot_ver[1] == 0x352E3156:    # TX BOOT V1.5
    payload90_key = "AE6DA6A206B70A5D89CC1D0884634643".decode("hex")
    payload90_ctr = "C461A8629F78081F6C3F0F5FC51607C3".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "0AB48861EA47036DC3E45B06A200B88E".decode("hex")
    payload98_ctr = "2FFDE0F331F6BA7DBCE7B2B228EDD0F0".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "A6BCA4B3EA6BBDF020F3F61268598608".decode("hex")
    payloadA0_ctr = "1897D379814B637E838C472B47C65C2D".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x689A0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "735B1BB11204B95DEF28338008AD9EEB".decode("hex")
    bootloader_ctr = "759421CBAB3C0164998705EAC843686E".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "1FE697859710A3E4A0A5F583EABB5360".decode("hex")
    assets_ctr = "B22FC3208D038C5025AB3716F466EFF3".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "534F6705DB4C19822A90D72A0E52871E".decode("hex")
    fw_ctr = "D29A20D59C1615CD84D09D95A4A5824D".decode("hex")
    fw_off = 0
    fw_size = 0x689A0
elif boot_ver[1] == 0x362E3156:    # TX BOOT V1.6
    payload90_key = "EB2CCE4A12A5E67D18BA7E7694BB668E".decode("hex")
    payload90_ctr = "541D5A701ACE180CF8FF4BEDA9420084".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "D21A5BCC99ACD2D06C785596A38E783A".decode("hex")
    payload98_ctr = "7C20F115244654025B14833A9AD949EE".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "9E1B0673697520D8431F121D93B97DEF".decode("hex")
    payloadA0_ctr = "205800A34B37097DFD7B7C4780C2F982".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x68AE0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "6D3210FFF1CF4514C0CEFD0D1FB1B975".decode("hex")
    bootloader_ctr = "E5DE043AC5D59CE37AF79F73B04309CB".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "EFB643AC023866040B25509F002C3239".decode("hex")
    assets_ctr = "B7651B5E1A5C17EF5067B447F5F7DDB9".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "376D7644BD386A377DDBFAEC8F25773B".decode("hex")
    fw_ctr = "2DF4E0DB583089B9873A53E8F420CA59".decode("hex")
    fw_off = 0
    fw_size = 0x68AE0
elif boot_ver[1] == 0x372E3156:    # TX BOOT V1.7
    payload90_key = "C6E8A08D888CF9CFCFABAA6593F5E209".decode("hex")
    payload90_ctr = "4161154C99F06E1E1464B7864C2CDDD9".decode("hex")
    payload90_off = 0xC0B990
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "C4A04B22B56E93445953C0B868C2C2F8".decode("hex")
    payload98_ctr = "250450BAB0DA9EACD3BA333CEAD4BA7B".decode("hex")
    payload98_off = 0xD014B0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F951256F5AB23C7EF1C2837D8581FA77".decode("hex")
    payloadA0_ctr = "0FAC52D6D8D7C212B2499810C9815232".decode("hex")
    payloadA0_off = 0xDBD740
    payloadA0_size = 0x68E30
    payloadA0_base = 0xA0000000
    
    bootloader_key = "E678C11F28849BC6DC525061A7C2C0D9".decode("hex")
    bootloader_ctr = "79029F017F0CA753E524145F362AC3E5".decode("hex")
    bootloader_off = 0x571EE0
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "767744996BAC7107FC2B3B4882033476".decode("hex")
    assets_ctr = "A298473FBFD787EDBA8DE2B50E0A25CA".decode("hex")
    assets_off = 0x592EA0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "3FBE84AD7FD4DACEA0A1A3401B548F3B".decode("hex")
    fw_ctr = "9378E449EF34C8FC5B204853F12CD01F".decode("hex")
    fw_off = 0
    fw_size = 0x68E30
elif boot_ver[1] == 0x382E3156:    # TX BOOT V1.8
    payload90_key = "C436E39A1BCD198F4200516242217010".decode("hex")
    payload90_ctr = "1840E301126AA9CA8F549CCDF3889294".decode("hex")
    payload90_off = 0xC0B990
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "CD16B01836D1A7587DA50F546CA68AC9".decode("hex")
    payload98_ctr = "BA4E9B943DCCDE3E1A91038773E7A1BA".decode("hex")
    payload98_off = 0xD014B0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "13F112C8668B8715C3BEDF24012CCE43".decode("hex")
    payloadA0_ctr = "58A06A2FAB8FC3C2D849A7E0D3687C25".decode("hex")
    payloadA0_off = 0xDBD740
    payloadA0_size = 0x68EA0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D361215F332E1D2487D656DE89DC60BB".decode("hex")
    bootloader_ctr = "7ACB8F5587023560AD3C565D4072B748".decode("hex")
    bootloader_off = 0x571EE0
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "5F6FDE101B5490272E94FC8B02E16598".decode("hex")
    assets_ctr = "A6EB0224D08BB2EAE9AF6A9C34BFE0A5".decode("hex")
    assets_off = 0x592EA0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "24ABD9DBBFA9B286464069CB43406126".decode("hex")
    fw_ctr = "753D3C5922B09B82FDF093B1EC0679F0".decode("hex")
    fw_off = 0
    fw_size = 0x68EA0
elif boot_ver[1] == 0x392E3156:    # TX BOOT V1.9
    payload90_key = "B9ADE0F7BD1EAE99F5D069766B191CF7".decode("hex")
    payload90_ctr = "0C71509233E4EAD601FA430CD92FB679".decode("hex")
    payload90_off = 0xC0F5D0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "C553D270DE004031B1A500C40856E051".decode("hex")
    payload98_ctr = "DE2551AC87A3CC5245A2D327395D8232".decode("hex")
    payload98_off = 0xD050F0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "363413B94F08FADBA77B201E5874A17D".decode("hex")
    payloadA0_ctr = "E59D8ED75CF96EAB5ADB14BD1210ADA4".decode("hex")
    payloadA0_off = 0xDC1380
    payloadA0_size = 0x674B0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "63742C20A5766B1A5D0550D6056958AB".decode("hex")
    bootloader_ctr = "ECE382D94917BA828804828DBC57E96F".decode("hex")
    bootloader_off = 0x575B20
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "E343335CBDFE5DFA8FD5271E42FE7C11".decode("hex")
    assets_ctr = "8982C3250EF72A55EF7E3597F2F2A28F".decode("hex")
    assets_off = 0x596AE0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "B2E2F4A27F6CA2238DA3090C665CB444".decode("hex")
    fw_ctr = "0E1EC09B58C73BC225CF0F5757311B20".decode("hex")
    fw_off = 0
    fw_size = 0x674B0
elif boot_ver[1] == 0x302E3256:    # TX BOOT V2.0
    payload90_key = "8545442BF5CB8848C752969379495834".decode("hex")
    payload90_ctr = "A39FE90850DF95CFEAD2330174AB8AA4".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "4BA67934D070999376E8A22E7A3E3DED".decode("hex")
    payload98_ctr = "3FDA98AC6C106E6C4AF0DB6E9F6B6976".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "B57345C1307C406F39161A03A0800C76".decode("hex")
    payloadA0_ctr = "535A4EF3B062A457736CAFFDB23A477A".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x68FF0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "25BB22426788BA349A6084F86F639966".decode("hex")
    bootloader_ctr = "A0F3C3D386912249AAC13D4080A34BAD".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "56CEFAA60C9228C084AE2F8F9BF05A9B".decode("hex")
    assets_ctr = "29B3EEF7629A3B266A304D2C2686CCEE".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "A644D3896171F04BFAFA145670CFA754".decode("hex")
    fw_ctr = "1D5ED868682B78C22B975533EC54B940".decode("hex")
    fw_off = 0
    fw_size = 0x68FF0
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x302E3256):    # TX BOOT V2.0.1
    payload90_key = "B98E565F67B2CE98362AA4BF4F63B285".decode("hex")
    payload90_ctr = "A1C674C08191F55DA125433207B74DB2".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "A3A8F9B91107049835FFE38CFAC02F03".decode("hex")
    payload98_ctr = "682EEF46CA0979B1A9DA6EE3CD977D0D".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F14481FA77A09437046AF1C453210562".decode("hex")
    payloadA0_ctr = "8583C354ED368877E1624FABB80D5631".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x6A2F0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "AEA54EBE9D700CC9334165ED88F52348".decode("hex")
    bootloader_ctr = "8350C5A81015E6BE4D8C1A8F6F9E833E".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "174BD6B29158444A775CCA63D2A5238E".decode("hex")
    assets_ctr = "4A6AA511A75A277162284451E36B4D82".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "474325E4147C63092E96EA693E7D1433".decode("hex")
    fw_ctr = "0414D05A071E83B3C64C3E61C8557255".decode("hex")
    fw_off = 0
    fw_size = 0x6A2F0
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x312E3256):        # TX BOOT V2.1
    payload90_key = "ECE308D1D6E3CFF988EC332C69A727ED".decode("hex")
    payload90_ctr = "4F1B32C985BB6B5BB93262FE3305C0AA".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "8BA66D50922849A87EC13E7A78DB0109".decode("hex")
    payload98_ctr = "C091B06C606A6E2AA4F06FB093691EB5".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "469F945F581F038A45618B20C7DF6F76".decode("hex")
    payloadA0_ctr = "A8959DB43802B08C891D0B55F2FB6794".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x6B240
    payloadA0_base = 0xA0000000
    
    bootloader_key = "0409FC24536E362DD080CBFD1498DFC6".decode("hex")
    bootloader_ctr = "7ABAE1B8335974D6B4E586D3B4D33196".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "D63BE485CB58716196055AFF004BF143".decode("hex")
    assets_ctr = "B673F5BD2C1B3C9174060552B598D7D6".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "4FB6882B92DA97D5DA233E660CBBF1E2".decode("hex")
    fw_ctr = "C21F0EF96CD2F18360089D8C65C63D88".decode("hex")
    fw_off = 0
    fw_size = 0x6B240
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x322E3256):        # TX BOOT V2.2
    payload90_key = "EE676C14CF4FC1B56B5E3CBCE6C6AA56".decode("hex")
    payload90_ctr = "6A4F46C609D042A506109DC67CF67321".decode("hex")
    payload90_off = 0xC39F10
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "817D7934FD5D10AEB4D3AC5B86D1D929".decode("hex")
    payload98_ctr = "602D2EE3EB8221FA5B4DDAE88A333567".decode("hex")
    payload98_off = 0xD2FA30
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "764A681CAC520674DAA3F07B743E412E".decode("hex")
    payloadA0_ctr = "A4FC4B6A126A3A7429351AE514D51847".decode("hex")
    payloadA0_off = 0xDEBCC0
    payloadA0_size = 0x71880
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FA0C4982AE476B3E1EA48BF49C07A680".decode("hex")
    bootloader_ctr = "138914FCE54056BA18C472FF35EAF2B4".decode("hex")
    bootloader_off = 0x576420
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "F1769A875BF70CF0C1D59326A4A45DB6".decode("hex")
    assets_ctr = "39B1C4AD9AC8C8949DF95E883B0B8261".decode("hex")
    assets_off = 0x5A9420
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "496F4B42816945B371662126BB192D49".decode("hex")
    fw_ctr = "B674C639CF3D522752320983DAB987C5".decode("hex")
    fw_off = 0
    fw_size = 0x71880
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x322E3256):    # TX BOOT V2.2.1
    payload90_key = "BCDDF8E03BB29E4AF53EA437B5A327A9".decode("hex")
    payload90_ctr = "1BEAA065F8A4AA120A3BB9786FCFF815".decode("hex")
    payload90_off = 0xC3A390
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "A18C98DD5BEEBC30C62F950C6C2D0133".decode("hex")
    payload98_ctr = "D07406E4BE4557967E7FACF0F006EF2E".decode("hex")
    payload98_off = 0xD2FEB0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "38C852F0B636FD231E7E3FC3CAD1C2E3".decode("hex")
    payloadA0_ctr = "3A50EB632ACEF74542C16623F31AB046".decode("hex")
    payloadA0_off = 0xDEC140
    payloadA0_size = 0x76F00
    payloadA0_base = 0xA0000000
    
    bootloader_key = "80EDE7A42FCE5EC197D1EAC37085981C".decode("hex")
    bootloader_ctr = "46FF431605844B997FA939B2053E668B".decode("hex")
    bootloader_off = 0x5768A0
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "AE2AEDAAF6D2BE55B4449A8593827D1E".decode("hex")
    assets_ctr = "79CDE541DAEF4E0CBFB4BC89A79DB992".decode("hex")
    assets_off = 0x5A98A0
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "908B117B241C5257DFB09FC20BE8943E".decode("hex")
    fw_ctr = "6A0BE18089129A58181155C5B7A9BBC4".decode("hex")
    fw_off = 0
    fw_size = 0x76F00
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x332E3256):    # TX BOOT V2.3
    payload90_key = "5057CD5B625D54EAC873D701E4242D2C".decode("hex")
    payload90_ctr = "DE702CDA2C10DFB4A5C301779D6C8E01".decode("hex")
    payload90_off = 0xC3A4B0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "E91CFD27867700954A69B6F25D3BB58A".decode("hex")
    payload98_ctr = "D614424E4876404863588BF93A5EDEFF".decode("hex")
    payload98_off = 0xD2FFD0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "C17826EC6E847F83C3AB34F5B686AADF".decode("hex")
    payloadA0_ctr = "0359E40094782F4F4E8BCD90D2440A70".decode("hex")
    payloadA0_off = 0xDEC260
    payloadA0_size = 0x7F360
    payloadA0_base = 0xA0000000
    
    bootloader_key = "708F97BE5663BE4D248A2F1F2FFCB02E".decode("hex")
    bootloader_ctr = "CFA497C913CADA90C23EA3135E931EE1".decode("hex")
    bootloader_off = 0x5769C0
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "595D289B1D5A19A59E2AE1EB213738D9".decode("hex")
    assets_ctr = "A456EE87BFF343CCC55A75E369CDE106".decode("hex")
    assets_off = 0x5A99C0
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "9CC31623621336122680BE55CE1205F8".decode("hex")
    fw_ctr = "83169D2F38590669158A9928EC0DD3CA".decode("hex")
    fw_off = 0
    fw_size = 0x7F360
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x342E3256):    # TX BOOT V2.4
    payload90_key = "F84650B75C01E9826116A08C0457C386".decode("hex")
    payload90_ctr = "D9BD23C8BAF707819922B2C10551BEF5".decode("hex")
    payload90_off = 0xC393A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "97788D3B3D092BB7FB1A3E788C3DD3EF".decode("hex")
    payload98_ctr = "63BDB1B13C354417B12D9DF312751570".decode("hex")
    payload98_off = 0xD2EEC0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "6423AA4095B57572D684568DB3712853".decode("hex")
    payloadA0_ctr = "E80E301C71518C31ACDFCCCE7A98DA2E".decode("hex")
    payloadA0_off = 0xDEB150
    payloadA0_size = 0x7DC60
    payloadA0_base = 0xA0000000
    
    bootloader_key = "776333894C7C7EF9819ADD4A00FC8E9D".decode("hex")
    bootloader_ctr = "16EC2B9012FA6849D3FE8BA51AB860C0".decode("hex")
    bootloader_off = 0x5778B0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "D6E524558716AB4495367CF6DBF4C4FB".decode("hex")
    assets_ctr = "F12B4BA9CBE043D470CE81FFD365FFF3".decode("hex")
    assets_off = 0x5A88B0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "BF7B24E0478167AD5E2F76C57DD41C59".decode("hex")
    fw_ctr = "514A33384321976B6F04BD02E587C1E8".decode("hex")
    fw_off = 0
    fw_size = 0x7DC60
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x342E3256):    # TX BOOT V2.4.1
    payload90_key = "A0BA31F12B44E3C51231731F8E7DCE3D".decode("hex")
    payload90_ctr = "EA3467C4C2DDCF9E2B237CEEFA8B2F73".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "CD24A287EF803E1A03862F5702F2213F".decode("hex")
    payload98_ctr = "EBAE7A97BD9EE2F85E592E5B6324DD43".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "AF7F69790C0BCE3BEC55402416683C85".decode("hex")
    payloadA0_ctr = "8803D2D2FA3630748AF548A45C982AF3".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x7DC50
    payloadA0_base = 0xA0000000
    
    bootloader_key = "2A882183AC20AE70CF8C18CCBD393945".decode("hex")
    bootloader_ctr = "CE5792D332C7D854567E698E3FB438F1".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "CFCFC912920E9BD17CD38829A5FB5B38".decode("hex")
    assets_ctr = "A052D42CB1BAB825F256315B980C5DEE".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "328E1D6E8C5E435F6D1C342090475C72".decode("hex")
    fw_ctr = "422571782D7CFB7E26CC0516801AD181".decode("hex")
    fw_off = 0
    fw_size = 0x7DC50
elif (boot_ver[1] == 0) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5
    payload90_key = "4B7FB43C99888DBAC0942D1B14A6AB36".decode("hex")
    payload90_ctr = "4FA7F1C5C2E056C371F36C38DA586B26".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "7CF57477016CAFE525DD570EFC0A4386".decode("hex")
    payload98_ctr = "F12CC7DD80DAC7C6F87F85A49855FA3A".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "B3356B83B3189050458D7F17D0275E3E".decode("hex")
    payloadA0_ctr = "94F7D32D84B2E34C809B9C9FD67A0777".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86280
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C196E7A1B6DB410B95C2EC30233B6ED3".decode("hex")
    bootloader_ctr = "1AFDBF2A89F090D0FFE5756CAB835631".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "8B21B2E6418DC8483277F87A94C3392F".decode("hex")
    assets_ctr = "2835032A4624915A757DD73F95166D3D".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "6E34454ACAB9824A8A2FD1DA8516CB50".decode("hex")
    fw_ctr = "51556B291B98251E7CF1AB867357B6E4".decode("hex")
    fw_off = 0
    fw_size = 0x86280
elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.1
    payload90_key = "1312378C696D73F5B9C0CAF435BF9E01".decode("hex")
    payload90_ctr = "30B0F050605DEE6544E882BDCAB00270".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "68EDAB3E2990E61AFBEF3131CE81AFBB".decode("hex")
    payload98_ctr = "36537950E3EC3CCE0310B29E44DFF398".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "97BD4243B2A51595CEBF10FFACD12709".decode("hex")
    payloadA0_ctr = "4CAEC0B13D430C9DCF08C1443F29888F".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86470
    payloadA0_base = 0xA0000000
    
    bootloader_key = "450BE513C651C282A81FD7900B9D7625".decode("hex")
    bootloader_ctr = "3B73FFA158508B95F85755B03A95E2BA".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "FE4878237692DFD1F337DC6886CCB140".decode("hex")
    assets_ctr = "F0AAA0969B69FDBCD9DD7E2CF8C4DA5E".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "B68AE8028313C1EF761FA1BE41E56A66".decode("hex")
    fw_ctr = "51B3A71C9C574F251835C88C322BEAEC".decode("hex")
    fw_off = 0
    fw_size = 0x86470
elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.2
    payload90_key = "5FCCC552C3A858E3650D60784C51E978".decode("hex")
    payload90_ctr = "649C698868CEB4FEFACB250E7E0E18FE".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "96FDA317909656484D6EE412959B189E".decode("hex")
    payload98_ctr = "B3ADA7BEB8695216B9CEF145DB18A053".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "E8C815198227E14A646E7465A682EB63".decode("hex")
    payloadA0_ctr = "176A50BE0A2481646C8CDFF0707099F9".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86490
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D3B64C8E57033058582643AB5065FFDF".decode("hex")
    bootloader_ctr = "E3A6EA967CF832D1DF2B731620EDBBDA".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "9E270E5E9A0EBDAB95589446793D7E78".decode("hex")
    assets_ctr = "A05CFA29C04FD14B267CB52795BE6262".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "AF18B196DE0E240655F8D8A59FAD585D".decode("hex")
    fw_ctr = "5F0251C985697D2216576991F4C7F5DD".decode("hex")
    fw_off = 0
    fw_size = 0x86490
elif (boot_ver[1] == 0x332E) and (boot_ver[0] == 0x352E3256):    # TX BOOT V2.5.3
    payload90_key = "06E663F93362E4A7D6CBBFCF4E790E54".decode("hex")
    payload90_ctr = "8DC308384AB3152E593106481EB40E61".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "6D5366A10514D10BC1E0A46DC0CEBA69".decode("hex")
    payload98_ctr = "B5C9BDEFF1ABCB7175C1939E63420910".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "1B850B5690AFC211CC994D83FEEE94DE".decode("hex")
    payloadA0_ctr = "530D7DF487C635901B8E689D03EFD902".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x864A0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "BA6DF53AB718F544755733C804B279D7".decode("hex")
    bootloader_ctr = "68DFA341E6F561D2D3A1598A83CDADB3".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "6208AB46E0227D8EACB9B08F8383BE8C".decode("hex")
    assets_ctr = "A8040F28D07989AFC6CFD19FCC5DFCB0".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "9165377EB58BABC3AAD9977F50299213".decode("hex")
    fw_ctr = "A6E10A060055BBB699A2FA9652C17D00".decode("hex")
    fw_off = 0
    fw_size = 0x864A0
else:
    exit()

# Decrypt second layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payload90_base), "wb")
f.write(aes_ctr_dec(b[payload90_off:payload90_off+payload90_size], payload90_key, payload90_ctr))
f.close()

# Decrypt third layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payload98_base), "wb")
f.write(aes_ctr_dec(b[payload98_off:payload98_off+payload98_size], payload98_key, payload98_ctr))
f.close()
    
# Decrypt fourth layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payloadA0_base), "wb")
f.write(aes_ctr_dec(b[payloadA0_off:payloadA0_off+payloadA0_size], payloadA0_key, payloadA0_ctr))
f.close()

# Create folder for the bootloader
if not os.path.exists("../bootloader/"):
    os.mkdir("../bootloader/")
os.chdir("../bootloader/")

# Decrypt SX OS bootloader's code and assets
f = open("bootloader_{0:08X}.bin".format(bootloader_base), "wb")
f.write(aes_ctr_dec(b[bootloader_off:bootloader_off+bootloader_size], bootloader_key, bootloader_ctr))
f.write(aes_ctr_dec(b[assets_off:assets_off+assets_size], assets_key, assets_ctr))
f.close()

os.chdir("../payloads/")

# Open final firmware binary (encrypted)
f = open("payload_A0000000.bin", "rb")
d = f.read()
f.close()

# Decrypt final firmware binary
f = open("payload_A0000000_dec.bin", "wb")
f.write(aes_ctr_dec(d[fw_off:fw_off+fw_size], fw_key, fw_ctr))
f.close()

# Open final firmware binary (decrypted)
f = open("payload_A0000000_dec.bin", "rb")
d = f.read()
f.close()

# Create folder for the patcher binaries
if not os.path.exists("../patcher/"):
    os.mkdir("../patcher/")
os.chdir("../patcher/")

if not boot_ver[0] and \
        (((boot_ver[1] >> 0x18) & 0xFF) < 0x32) and \
        (((boot_ver[1] >> 0x08) & 0xFF) < 0x32):           # Old layout
    patcher_size = struct.unpack("I", d[0x10:0x14])[0]
    patcher_off = struct.unpack("I", d[0x14:0x18])[0]
    patcher_base = struct.unpack("I", d[0x18:0x1C])[0]
    patcher_crc = struct.unpack("I", d[0x1C:0x20])[0]
    patcher_hash = struct.unpack("8I", d[0x50:0x70])
        
    # Parse and store the PK11 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x20:0x24])[0]
    patcher_off = struct.unpack("I", d[0x24:0x28])[0]
    patcher_base = struct.unpack("I", d[0x28:0x2C])[0]
    patcher_crc = struct.unpack("I", d[0x2C:0x30])[0]
    patcher_hash = struct.unpack("8I", d[0x70:0x90])

    # Parse and store the KIP1/INI1 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x30:0x34])[0]
    patcher_off = struct.unpack("I", d[0x34:0x38])[0]
    patcher_base = struct.unpack("I", d[0x38:0x3C])[0]
    patcher_crc = struct.unpack("I", d[0x3C:0x40])[0]
    patcher_hash = struct.unpack("8I", d[0x90:0xB0])
        
    # Parse and store the kernel patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    # Create folder for the actual firmware binaries
    if not os.path.exists("../firmware/"):
        os.mkdir("../firmware/")
    os.chdir("../firmware/")
        
    kip_size = struct.unpack("I", d[0x40:0x44])[0]
    kip_off = struct.unpack("I", d[0x44:0x48])[0]
    kip_base = struct.unpack("I", d[0x48:0x4C])[0]
    kip_crc = struct.unpack("I", d[0x4C:0x50])[0]
    kip_hash = struct.unpack("8I", d[0xB0:0xD0])

    # Parse and store the Loader KIP1
    f = open("kip_{0:08X}.bin".format(kip_base), "wb")
    f.write(d[kip_off:kip_off+kip_size])
    f.close()
else:                                                                                       # New layout
    patcher_size = struct.unpack("I", d[0x00:0x04])[0]
    patcher_off = struct.unpack("I", d[0x04:0x08])[0]
    patcher_base = struct.unpack("I", d[0x08:0x0C])[0]
    patcher_crc = struct.unpack("I", d[0x0C:0x10])[0]
    patcher_hash = struct.unpack("8I", d[0x10:0x30])
        
    # Parse and store the PK11 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x30:0x34])[0]
    patcher_off = struct.unpack("I", d[0x34:0x38])[0]
    patcher_base = struct.unpack("I", d[0x38:0x3C])[0]
    patcher_crc = struct.unpack("I", d[0x3C:0x40])[0]
    patcher_hash = struct.unpack("8I", d[0x40:0x60])

    # Parse and store the KIP1/INI1 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x60:0x64])[0]
    patcher_off = struct.unpack("I", d[0x64:0x68])[0]
    patcher_base = struct.unpack("I", d[0x68:0x6C])[0]
    patcher_crc = struct.unpack("I", d[0x6C:0x70])[0]
    patcher_hash = struct.unpack("8I", d[0x70:0x90])
        
    # Parse and store the kernel patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    # Create folder for the actual firmware binaries
    if not os.path.exists("../firmware/"):
        os.mkdir("../firmware/")
    os.chdir("../firmware/")
        
    kip_size = struct.unpack("I", d[0x90:0x94])[0]
    kip_off = struct.unpack("I", d[0x94:0x98])[0]
    kip_base = struct.unpack("I", d[0x98:0x9C])[0]
    kip_crc = struct.unpack("I", d[0x9C:0xA0])[0]
    kip_hash = struct.unpack("8I", d[0xA0:0xC0])

    # Parse and store the Loader KIP1
    f = open("kip_{0:08X}.bin".format(kip_base), "wb")
    f.write(d[kip_off:kip_off+kip_size])
    f.close()
    
    kip_size = struct.unpack("I", d[0xC0:0xC4])[0]
    kip_off = struct.unpack("I", d[0xC4:0xC8])[0]
    kip_base = struct.unpack("I", d[0xC8:0xCC])[0]
    kip_crc = struct.unpack("I", d[0xCC:0xD0])[0]
    kip_hash = struct.unpack("8I", d[0xD0:0xF0])

    # Parse and store the sm KIP1
    f = open("kip_{0:08X}.bin".format(kip_base), "wb")
    f.write(d[kip_off:kip_off+kip_size])
    f.close()
        
    # New KIP file in V1.3+
    if boot_ver[0] or \
            (((boot_ver[1] >> 0x18) & 0xFF) >= 0x33) or \
            (((boot_ver[1] >> 0x08) & 0xFF) >= 0x32):
        kip_size = struct.unpack("I", d[0xF0:0xF4])[0]
        kip_off = struct.unpack("I", d[0xF4:0xF8])[0]
        kip_base = struct.unpack("I", d[0xF8:0xFC])[0]
        kip_crc = struct.unpack("I", d[0xFC:0x100])[0]
        kip_hash = struct.unpack("8I", d[0x100:0x120])

        # Parse and store the fs.mitm KIP1
        f = open("kip_{0:08X}.bin".format(kip_base), "wb")
        f.write(d[kip_off:kip_off+kip_size])
        f.close()
        
# New application files in V1.4+
if boot_ver[0] or \
        (((boot_ver[1] >> 0x18) & 0xFF) >= 0x34) or \
        (((boot_ver[1] >> 0x08) & 0xFF) >= 0x32):
    app_region_off = struct.unpack("I", b[0x4C:0x50])[0]
    app_region_size = (len(b) - app_region_off)
    app_region = aes_ctr_dec(b[app_region_off:app_region_off+app_region_size], fw_key, fw_ctr)
    app_header_off = 0
    app_header_size = 0x310
    app_header = app_region[app_header_off:app_header_size]
    app_entry_count = struct.unpack("I", app_header[0x00:0x04])[0]
    app_entry_size = 0x30
    
    # Create folder for the application binaries
    if not os.path.exists("../apps/"):
        os.mkdir("../apps/")
    os.chdir("../apps/")
    
    for i in xrange(app_entry_count):
        app_magic = struct.unpack("2I", app_header[0x10 + i * app_entry_size:0x18 + i * app_entry_size])
        app_hash = struct.unpack("8I", app_header[0x18 + i * app_entry_size:0x38 + i * app_entry_size])
        app_off = struct.unpack("I", app_header[0x38 + i * app_entry_size:0x3C + i * app_entry_size])[0]
        app_size = struct.unpack("I", app_header[0x3C + i * app_entry_size:0x40 + i * app_entry_size])[0]
        
        # ROMMENU
        if ((app_magic[0] == 0x4D454E55) and (app_magic[1] == 0x00524F4D)):
            f = open("ROMMENU.bin", "wb")
            f.write(app_region[app_off:app_off+app_size])
            f.close()
            
        # HBMENU
        if ((app_magic[0] == 0x4D454E55) and (app_magic[1] == 0x00004842)):
            f = open("HBMENU.bin", "wb")
            f.write(app_region[app_off:app_off+app_size])
            f.close()