# !pip install BitVector
from BitVector import *
# print("Two One Nine Two")

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

AES_modulus = BitVector(bitstring='100011011')

# bv1 = BitVector(hexstring="02")
# bv2 = BitVector(hexstring="63")
# bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
b2= BitVector(hexstring='02')
# print(bv3.get_bitvector_in_hex())

key="hjdggdjsfhjhsdgfjsdf125@#2"
text="hello world 125 @#%"

def convert_int_to_hex(key):
    # Convert the key to hexadecimal representation
    hex_key = hex(key).zfill(16)

    return hex_key

def split_hex(hex_string):
    # Ensure the length of the hex string is a multiple of 2
    if len(hex_string) % 2 != 0:
        raise ValueError("Hexadecimal string length must be a multiple of 2")

    # Convert each pair of hexadecimal digits into a character
    char_list = [(hex_string[i:i+2]) for i in range(2, len(hex_string), 2)]

    # Join the characters into a single string
    # char_representation = ''.join(char_list)
    # print(len(char_list))

    return char_list



def string_to_hex(string):
    if(type(string)==int):
      hx=convert_int_to_hex(string)
      lst=split_hex(hx)
      hex_string=""
      for h in lst:
        hex_string+=h+","
      return hex_string[:-1]
    else:
      hex_string = ""
      for char in string:
          hex_string += hex(ord(char))[2:]+","  # [2:] removes the '0x' prefix
      return hex_string[:-1]


def split_keys(hx_key):
  w=[[0] * 4 for _ in range(4)]
  num_key=hx_key.split(",")
  j=0
  for i in num_key:
    # x=int(i,16)
    if(j>=16):
      break
    w[int(j/4)][j%4]=i
    j+=1
    # print(type(x))
  if(j<16):
    for i in range(j,16):
      w[int(i/4)][i%4]=hex(ord('#'))[2:]
  return w


def g_key_cal(key,shft,rc):
    shfted_key=key[shft:]+key[:shft]
    round_key=[rc,'00','00','00']
    gkey=[0]*4
    i=0
    for sk in shfted_key:
      hk=BitVector(hexstring=sk)
      int_val = hk.intValue()
      s = Sbox[int_val]
      s = BitVector(intVal=s, size=8)
      x=int(s.get_bitvector_in_hex(),16)
      t=BitVector(hexstring=round_key[i])
      y=t.intValue()
      z=x^y
      gkey[i]=hex(z)[2:]
      # print(hex(z))
      # gkey[i] =hex(int(round_key[i],16)+int(Sbox[int_val],16))
      i+=1
    return gkey

def xor(arr1,arr2,l):
  arr=[0]*l
  # print(len(arr1))
  # print(len(arr2))
  for i in range(0,l):
    xs=BitVector(hexstring=arr1[i])
    x=xs.intValue()
    ys=BitVector(hexstring=arr2[i])
    y=ys.intValue()
    z=x^y
    arr[i]=hex(z)[2:]
  return arr

def mat_xor(mat1,mat2,l):
  arr=[[0]*l for i in range(0,l)]
  for i in range(0,l):
    for j in range (0,l):
      # print(type(mat1[i][j]))
      x=int(mat1[i][j],16)^int(mat2[i][j],16)
      arr[i][j]=hex(x)[2:]
  return arr


all_keys=list()
# all_keys.append(w)
def extend_keys(key,r,rc):
  x=[0]*4
  if(r==10):
    return
  r+=1
  g3=g_key_cal(key[3],1,rc)
  x[0]=xor(key[0],g3,4)
  x[1]=xor(key[1],x[0],4)
  x[2]=xor(key[2],x[1],4)
  x[3]=xor(key[3],x[2],4)
  all_keys.append(x)
  # print(type(rc))
  rc=BitVector(hexstring=rc)
  rc = b2.gf_multiply_modular(rc, AES_modulus, 8)
  rc=rc.intValue()
  rc=hex(rc)[2:]
  extend_keys(x,r,rc)

  return x

def get_all_keys(key):
  key=string_to_hex(key)
  w=split_keys(key)
  all_keys.append(w)
  # print(w)
  rc="01"
  extend_keys(w,0,rc)
  return all_keys


# print(all_keys[10])

# encrypt#####
def col_order_mat(mat,l):
  arr=[[0]*l for i in range(0,l)]
  for i in range (0,l):
    for j in range(0,l):
      arr[i][j]=mat[j][i]
  return arr

def sub(mat,l):
  for i in range(0,l):
    for j in range (0,l):
      hk=BitVector(hexstring=mat[i][j])
      int_val = hk.intValue()
      s = Sbox[int_val]
      s = BitVector(intVal=s, size=8)
      mat[i][j]=s.get_bitvector_in_hex()
  return mat


def left_shifter(mat,l):
  arr=[0]*l
  for i in range(0,l):
    arr=mat[i]
    arr=arr[i:]+arr[:i]
    mat[i]=arr
  return mat

def mixer(mat,l):

  result=[[0]*l for i in range(0,l)]
  for i in range(0,l):
      for j in range(0,l):
          x=0
          for k in range(0,l):
            mx=Mixer[i][k]
            v=mat[k][j]
            bv = BitVector(hexstring=v)
            br=mx.gf_multiply_modular(bv, AES_modulus, 8)
            br=br.intValue()
            x=x^br
          result[i][j] =hex(x)[2:]
  return result


def round_operations(s_mat,r):
  for i in range(1,11):

    sub_mat=sub(s_mat,4)
    shft_mat=left_shifter(sub_mat,4)
    s_key=col_order_mat(all_keys[i],4)
    if(i<10):
      mx=mixer(shft_mat,4)
    else:
      mx=shft_mat
    res_mat=mat_xor(mx,s_key,4)
    r+=1
    s_mat=res_mat
    # round_operations(res_mat,r)
  return s_mat

def produce_cipher_text(mat):
  c_text=""
  for i in range (len(mat)):
    for j in range (len(mat)):
      c_text+=mat[i][j]+","
  return c_text[:-1]

def round0(r,text):
  s_mat0=col_order_mat(text,4)
  s_key0=col_order_mat(all_keys[r],4)
  s0=mat_xor(s_key0,s_mat0,4)
  return s0

def encrypt(text,key):
    # get_all_keys(key)
    tx_hx=string_to_hex(text)
    text_split=split_keys(tx_hx)
    s0=round0(0,text_split)
    s1=round_operations(s0,1)
    s1=col_order_mat(s1,4)
    c_text=produce_cipher_text(s1)
    return c_text



# decrypt########

def round10(r,text):
  s_mat0=col_order_mat(text,4)
  s_key0=col_order_mat(all_keys[r],4)
  s0=mat_xor(s_key0,s_mat0,4)
  return s0

def inv_sub(mat,l):
  for i in range(0,l):
    for j in range (0,l):
      hk=BitVector(hexstring=mat[i][j])
      int_val = hk.intValue()
      s = InvSbox[int_val]
      s = BitVector(intVal=s, size=8)
      mat[i][j]=s.get_bitvector_in_hex()
  return mat

def right_shifter(mat,l):
  arr=[0]*l
  for i in range(0,l):
    arr=mat[i]
    arr=arr[-i:]+arr[:-i]
    mat[i]=arr
  return mat

def inv_mixer(mat,l):

  result=[[0]*l for i in range(0,l)]
  for i in range(0,l):
      for j in range(0,l):
          x=0
          for k in range(0,l):
            mx=InvMixer[i][k]
            v=mat[k][j]
            bv = BitVector(hexstring=v)
            br=bv.gf_multiply_modular(mx, AES_modulus, 8)
            br=br.intValue()
            x=x^br
          result[i][j] =hex(x)[2:]
  return result

def inv_round_operations(s_mat,r):
  for i in range(9,-1,-1):

    shft_mat=right_shifter(s_mat,4)
    sub_mat=inv_sub(shft_mat,4)
    
    s_key=col_order_mat(all_keys[i],4)

    res_mat=mat_xor(sub_mat,s_key,4)
    if(i>0):
      mx=inv_mixer(res_mat,4)
    else:
      mx=res_mat
    
    s_mat=mx
    # round_operations(res_mat,r)
  return s_mat

def hex_to_string(hex_str):
  massage=""
  num_key=hex_str.split(",")
  for i in num_key:
    massage+=chr(int(i,16))
    # print(chr(int(i,16)))
  return massage

def decrypt(text,key):
    c_mat=split_keys(text)
    d_s10=round10(10,c_mat)
    ds0=inv_round_operations(d_s10,9)
    col_mat=col_order_mat(ds0,4)
    data=produce_cipher_text(col_mat)
    massage=hex_to_string(data)
    return massage


# tests
get_all_keys(key)

t=encrypt(text,key)
print(t)


d=decrypt(t,key)
print(d)