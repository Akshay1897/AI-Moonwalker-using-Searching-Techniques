import sys
import heapq
import math
import time

class mars_rover():
    def __init__(self):
        input_fp=open("input_shamanth.txt","r")
        self.algorithm=input_fp.readline()
        dimension=input_fp.readline().split(" ")
        self.w,self.h=int(dimension[0]),int(dimension[1])
        self.elevation_matrix=[[-1]*self.w for x in range(self.h)]
        landing_coordinates=input_fp.readline().split(" ")
        self.starting_point=(int(landing_coordinates[0]),int(landing_coordinates[1]))
        self.max_elevation=int(input_fp.readline())
        self.number_targetsites=int(input_fp.readline())
        self.target_list=[None]*self.number_targetsites
        for i in range(self.number_targetsites):
            target=input_fp.readline().split(" ")
            self.target_list[i]=(int(target[0]),int(target[1]))
        for i in range(self.h):
            width=input_fp.readline().split(" ")
            for j in range(self.w):
                self.elevation_matrix[i][j]=int(width[j])

        self.output_fp=open("output.txt","w")
    def checkqueue(self,queue,current_node,new_node,cost):
        for i in range(len(queue)):
            if(queue[i][1]==new_node and cost<queue[i][0]):
                queue[i][0]=cost
                queue[i][2]=current_node[1]
                heapq.heapify(queue)
                break
    def calculate_heuristic(self,start,target):
        start_x,start_y=start
        target_x,target_y=target

        return math.sqrt((target_x-start_x)**2+(target_y-start_y)**2)
        
                

    def queuing_function(self,current_node,queue,visited,target):
        if self.algorithm=='BFS\n':
            x,y=current_node[0]
            if(x+1<self.w):
                if(abs(self.elevation_matrix[y][x+1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y][x+1]!=1):
                    queue.append([(x+1,y),current_node[1]+1,current_node[0]])
                    visited[y][x+1]=1
            if(x+1<self.w and y+1<self.h):
                if(abs(self.elevation_matrix[y+1][x+1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y+1][x+1]!=1):
                    queue.append([(x+1,y+1),current_node[1]+1,current_node[0]])
                    visited[y+1][x+1]=1
            if(y+1<self.h):
                if(abs(self.elevation_matrix[y+1][x]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y+1][x]!=1):
                    queue.append([(x,y+1),current_node[1]+1,current_node[0]])
                    visited[y+1][x]=1
            if(y+1<self.h and x-1>=0):
                if(abs(self.elevation_matrix[y+1][x-1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y+1][x-1]!=1):
                    queue.append([(x-1,y+1),current_node[1]+1,current_node[0]])
                    visited[y+1][x-1]=1
            if(x-1>=0):
                if(abs(self.elevation_matrix[y][x-1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y][x-1]!=1):
                    queue.append([(x-1,y),current_node[1]+1,current_node[0]])
                    visited[y][x-1]=1
            if(y-1>=0 and x-1>=0):
                if(abs(self.elevation_matrix[y-1][x-1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y-1][x-1]!=1):
                    queue.append([(x-1,y-1),current_node[1]+1,current_node[0]])
                    visited[y-1][x-1]=1
            if(y-1>=0):
                if(abs(self.elevation_matrix[y-1][x]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y-1][x]!=1):
                    queue.append([(x,y-1),current_node[1]+1,current_node[0]])
                    visited[y-1][x]=1
            if(y-1>=0 and x+1<self.w):
                if(abs(self.elevation_matrix[y-1][x+1]-self.elevation_matrix[y][x])<=self.max_elevation and visited[y-1][x+1]!=1):
                    queue.append([(x+1,y-1),current_node[1]+1,current_node[0]])
                    visited[y-1][x+1]=1
                
                    
                    
        if self.algorithm=='UCS\n':
            x,y=current_node[1]
            if(x+1<self.w):
                if(abs(self.elevation_matrix[y][x+1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y][x+1]!=1):
                        heapq.heappush(queue,[current_node[0]+10,(x+1,y),current_node[1]])
                        visited[y][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y),current_node[0]+10)
            if(x+1<self.w and y+1<self.h):
                if(abs(self.elevation_matrix[y+1][x+1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y+1][x+1]!=1):
                        heapq.heappush(queue,[current_node[0]+14,(x+1,y+1),current_node[1]])
                        visited[y+1][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y+1),current_node[0]+14)
            if(y+1<self.h):
                 if(abs(self.elevation_matrix[y+1][x]-self.elevation_matrix[y][x])<=self.max_elevation):
                     if(visited[y+1][x]!=1):
                         heapq.heappush(queue,[current_node[0]+10,(x,y+1),current_node[1]])
                         visited[y+1][x]=1
                     else:
                         self.checkqueue(queue,current_node,(x,y+1),current_node[0]+10)
            if(y+1<self.h and x-1>=0):
                if(abs(self.elevation_matrix[y+1][x-1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y+1][x-1]!=1):
                        heapq.heappush(queue,[current_node[0]+14,(x-1,y+1),current_node[1]])
                        visited[y+1][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y+1),current_node[0]+14)
            if(x-1>=0):
                if(abs(self.elevation_matrix[y][x-1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y][x-1]!=1):
                        heapq.heappush(queue,[current_node[0]+10,(x-1,y),current_node[1]])
                        visited[y][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y),current_node[0]+10)
            if(y-1>=0 and x-1>=0):
                if(abs(self.elevation_matrix[y-1][x-1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y-1][x-1]!=1):
                        heapq.heappush(queue,[current_node[0]+14,(x-1,y-1),current_node[1]])
                        visited[y-1][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y-1),current_node[0]+14)
            if(y-1>=0):
                if(abs(self.elevation_matrix[y-1][x]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y-1][x]!=1):
                        heapq.heappush(queue,[current_node[0]+10,(x,y-1),current_node[1]])
                        visited[y-1][x]=1
                    else:
                        self.checkqueue(queue,current_node,(x,y-1),current_node[0]+10)

            if(y-1>=0 and x+1<self.w):
                if(abs(self.elevation_matrix[y-1][x+1]-self.elevation_matrix[y][x])<=self.max_elevation):
                    if(visited[y-1][x+1]!=1):
                        heapq.heappush(queue,[current_node[0]+14,(x+1,y-1),current_node[1]])
                        visited[y-1][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y-1),current_node[0]+14)
            
        if self.algorithm=='A*\n':
            x,y=current_node[1]
            if(x+1<self.w):
                elevation_difference=abs(self.elevation_matrix[y][x+1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x+1,y),target)+ current_node[0]+10+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y][x+1]!=1):
                        heapq.heappush(queue,[cost,(x+1,y),current_node[1]])
                        visited[y][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y),cost)
            if(x+1<self.w and y+1<self.h):
                elevation_difference=abs(self.elevation_matrix[y+1][x+1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x+1,y+1),target)+current_node[0]+14+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y+1][x+1]!=1):
                        heapq.heappush(queue,[cost,(x+1,y+1),current_node[1]])
                        visited[y+1][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y+1),cost)
            if(y+1<self.h):
                 elevation_difference=abs(self.elevation_matrix[y+1][x]-self.elevation_matrix[y][x])
                 if(elevation_difference<=self.max_elevation):
                     cost=self.calculate_heuristic((x,y+1),target)+ current_node[0]+10+elevation_difference-self.calculate_heuristic((x,y),target)
                     if(visited[y+1][x]!=1):
                         heapq.heappush(queue,[cost,(x,y+1),current_node[1]])
                         visited[y+1][x]=1
                     else:
                         self.checkqueue(queue,current_node,(x,y+1),cost)
            if(y+1<self.h and x-1>=0):
                elevation_difference=abs(self.elevation_matrix[y+1][x-1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x-1,y+1),target)+ current_node[0]+14+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y+1][x-1]!=1):
                        heapq.heappush(queue,[cost,(x-1,y+1),current_node[1]])
                        visited[y+1][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y+1),cost)
            if(x-1>=0):
                elevation_difference=abs(self.elevation_matrix[y][x-1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x-1,y),target)+ current_node[0]+10+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y][x-1]!=1):
                        heapq.heappush(queue,[cost,(x-1,y),current_node[1]])
                        visited[y][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y),cost)
            if(y-1>=0 and x-1>=0):
                elevation_difference=abs(self.elevation_matrix[y-1][x-1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x-1,y-1),target)+ current_node[0]+14+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y-1][x-1]!=1):
                        heapq.heappush(queue,[cost,(x-1,y-1),current_node[1]])
                        visited[y-1][x-1]=1
                    else:
                        self.checkqueue(queue,current_node,(x-1,y-1),cost)
            if(y-1>=0):
                elevation_difference=abs(self.elevation_matrix[y-1][x]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x,y-1),target)+ current_node[0]+10+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y-1][x]!=1):
                        heapq.heappush(queue,[cost,(x,y-1),current_node[1]])
                        visited[y-1][x]=1
                    else:
                        self.checkqueue(queue,current_node,(x,y-1),cost)

            if(y-1>=0 and x+1<self.w):
                elevation_difference=abs(self.elevation_matrix[y-1][x+1]-self.elevation_matrix[y][x])
                if(elevation_difference<=self.max_elevation):
                    cost=self.calculate_heuristic((x+1,y-1),target)+ current_node[0]+14+elevation_difference-self.calculate_heuristic((x,y),target)
                    if(visited[y-1][x+1]!=1):
                        heapq.heappush(queue,[cost,(x+1,y-1),current_node[1]])
                        visited[y-1][x+1]=1
                    else:
                        self.checkqueue(queue,current_node,(x+1,y-1),cost)        


            
            
    def findoptimal_helper_ucs(self,starting_point,target,result_path,queue,visited):
        initial_cost=0
        x,y=starting_point
        initial_cost_a=self.calculate_heuristic((x,y),target)
        parent=(-1,-1)
        if self.algorithm=='UCS\n':
            heapq.heappush(queue,[initial_cost,starting_point,parent])
        else:
            heapq.heappush(queue,[initial_cost_a,starting_point,parent])
        visited[y][x]=1

        while(True):
            if(len(queue)==0):
                return -1
            current_node=heapq.heappop(queue)
            result_path.update({current_node[1]:current_node[2]})
            if(current_node[1]==target):
                print(current_node[0])
                return 1
            self.queuing_function(current_node,queue,visited,target)
        
    def findoptimal_helper_bfs(self,starting_point,target,result_path,queue,visited):
        initial_cost=0
        parent=(-1,-1)
        queue.append([starting_point,initial_cost,parent])
        x,y=starting_point
        visited[y][x]=1
        while(True):
            if(len(queue)==0):
                return -1
            current_node=queue[0]
            del(queue[0])
            result_path.update({current_node[0]:current_node[2]})
            if(current_node[0]==target):
                return 1
            self.queuing_function(current_node,queue,visited,target)
            
    def find_optimal_path(self):
        for i in range(self.number_targetsites):
            result_path={}
            queue=[]
            visited=[[0]*self.w for x in range(self.h)]
            if self.algorithm=='BFS\n':
                result=self.findoptimal_helper_bfs(self.starting_point,self.target_list[i],result_path,queue,visited)
            elif(self.algorithm=='UCS\n' or self.algorithm=='A*\n'):
                result=self.findoptimal_helper_ucs(self.starting_point,self.target_list[i],result_path,queue,visited)

            if result==1:
                temp=self.target_list[i]
                out=[]
                while(temp!=self.starting_point):
                    x,y=temp
                    out.insert(0,str(x)+','+str(y))
                    temp=result_path[temp]
                x,y=temp
                out.insert(0,str(x)+','+str(y))
                self.output_fp.write(" ".join(out))
                if(i!=self.number_targetsites-1):
                    self.output_fp.write('\n')

            elif(result==-1):
                self.output_fp.write("FAIL")
                if(i!=self.number_targetsites-1):
                    self.output_fp.write('\n')
                
                    
       
def main():
    
    new_rover=mars_rover()
    st=time.time()
    new_rover.find_optimal_path()
    et=time.time()
    print(et-st)
    
if __name__=='__main__':
    main()
