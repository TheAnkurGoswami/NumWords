def numwords(num):
    if num>99999999999999:
        raise Exception('Value should not exceed 99999999999999')
    digits_to_words={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    numbers_to_words={'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
                      '17':'seventeen','18':'eighteen','19':'nineteen'}
    tens={'2':'twenty','3':'thirty','4':'fourty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
    
    def batches_to_words(batch):
        string=''
        if len(batch)==3 and batch[2]!='0':
            string+=digits_to_words[batch[2]]+' hundred'
        if len(batch)>=2 and batch[1]!='0':
            if 9<int(batch[1::-1])<20:
                string+=' '+numbers_to_words[batch[1::-1]]
            else:
                string+=' '+tens[batch[1]]
        if len(batch)>=1 and batch[0]!='0':
            if 9<int(batch[1::-1])<20:
                pass
            else:
                string+=' '+digits_to_words[batch[0]]
        return (batch[::-1],string)
    
    num_=str(num)
    num_=num_[::-1]    #Reversing the number
    
    batch_list=[]
    prev=0
    div=len(num_)//3
    for i in range(div):
        curr=3*i+2
        batch_list.append(num_[prev:curr+1])
        prev=curr+1
        
    if len(num_)%3!=0:
        div+=1
        batch_list.append(num_[prev:])
    print(batch_list)
    
    counter=-1
    string=''
    List=[' thousand',' million',' billion',' trillion','']
    for batch in batch_list:
        if counter==-1:
            string=batches_to_words(batch)[1]+' '+string
        else:
            string=batches_to_words(batch)[1]+List[counter]+' '+string      
        counter+=1
    
    return string.strip().title()
