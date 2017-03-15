import sys

class Automata(object):
    def __init__(self, n=0, states=set(), simbols=set(), term=set(), state_transition_function=[]):
        self.n = n
        self.states = states
        self.simbols = simbols
        self.term = term
        self.state_transition_function = state_transition_function
    
    def read_transition(self, s):
        a, b, c = s.split()
        self.simbols.add(b)
        self.state_transition_function[int(a)][b] = int(c)

    def dfs(self, i):
        self.states.add(i)
        for v in (self.state_transition_function[i][x] for x in self.simbols):
            if v not in self.states:
                self.dfs(v)

    def read_automata(self):
        s = sys.stdin.readline()
        n, k, l = s.split()
        n, l = int(n), int(l)
        self.n = n

        s = sys.stdin.readline()
        self.term = set(map(int, s.split()))

        self.state_transition_function = [{} for i in xrange(n)]
        for i in xrange(n*l):
            self.read_transition(sys.stdin.readline())

        self.states = set()
        self.dfs(0)
        self.term = self.term.intersection(self.states)

    def get_min_automata_fast(self):
        term = self.term
        states = self.states
        simbols = self.simbols
        state_transition_function = self.state_transition_function

        q = []
        a = []
        s1 = term
        s2 = states.difference(term)
        s1 = list(s1)
        s1.sort()
        s2 = list(s2)
        s2.sort()
        if s1:
            a.append(s1)
            for x in simbols:
                q.append((s1, x))
        if s2:
            a.append(s2)
            for x in simbols:
                q.append((s2, x))

        i=0
        while i < len(q):
            C, c = q[i]
            i += 1
            if C not in a:
                continue
            a_new = []
            for M in a:
                s1 = [v for v in M if state_transition_function[v][c] in C]
                s2 = [v for v in M if state_transition_function[v][c] not in C]
                if s1 and s2: 
                    a_new.append(s1)
                    a_new.append(s2)
                    for y in simbols:
                        q.append((s1, y))
                        q.append((s2, y))
                else:
                    a_new.append(M)
            a = a_new
        #print a
        return len(a)
        

       
        

def main():
    A = Automata()
    A.read_automata()
    print A.get_min_automata_fast()

main()


        
    
    

    
        
