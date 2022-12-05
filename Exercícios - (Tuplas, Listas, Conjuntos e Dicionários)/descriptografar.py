alf_normal = input()
alf_cif = input()

mapeamento = dict(zip(alf_cif, alf_normal))

mensagem_cifrada = input()

msg = ''.join(mapeamento[l] if l in mapeamento else l for l in mensagem_cifrada)


print(msg)


#for l in mensagem_cifrada:
 #   if l in mapeamento:
   #     msg += mapeamento[l]
    #else:
     #   msg += l
    # msg += mapeamento[l] if l in mapeamento else l

    
