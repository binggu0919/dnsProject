class banjoriDGA :

    def __init__(self,domain) :
        self.domain = domain

    def map_to_lowercase_letter(self,s):
        return ord('a') + ((s - ord('a')) % 26)

    def next_domain(self,domain):
        dl = [ord(x) for x in list(domain)]
        dl[0] = self.map_to_lowercase_letter(dl[0] + dl[3])
        dl[1] = self.map_to_lowercase_letter(dl[0] + 2*dl[1])
        dl[2] = self.map_to_lowercase_letter(dl[0] + dl[2] - 1)
        dl[3] = self.map_to_lowercase_letter(dl[1] + dl[2] + dl[3])
        return ''.join([chr(x) for x in dl])

    def domain_generate(self,num) :
        # seed = 'earnestnessbiophysicalohax.com' # 15372 equal to 0 (seed = 0)
        for i in range(num):
            print(self.domain)
            self.domain = self.next_domain(self.domain)
