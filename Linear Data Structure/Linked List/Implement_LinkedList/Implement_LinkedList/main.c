//
//  main.c
//  Implement_LinkedList
//
//  Created by 곽보선 on 2021/08/31.
//

#include <stdio.h>
#include <stdlib.h>    // malloc, free

// 연결 리스트의 노드 구조체
typedef struct NODE {
    
    int data;             // 데이터를 저장할 변수
    struct NODE* link;    // 다음 노드의 주소를 저장할 포인터(자기참조 구조체 포인터) : "노드 구조체의 주소" 저장
      
}NODE;

//n번째 노드에 저장되어 있는 값을 불러오는 함수
char get(struct NODE *target,int n){
    
    for(int i=0;i<n;i++){
        target=target->link;
    }
    return target->data;
}

// 기준 노드 뒤에 노드를 추가하는 함수
void insert(struct NODE *head, int pos, int data){
    
    NODE* cur = head;
    NODE* new = malloc(sizeof(NODE));             // new node
    new->data = data;                             // 데이터 저장
    new->link = NULL;
    
    if (pos == 0){
        new->link = head->link;                   // head 노드의 다음 노드를 지정
        head->link = new;                         // head 노드의 다음 노드에 새 노드를 지정
    }
    else{
        int cnt = 0;
        while(cnt != pos){
            if(cnt == (pos-1)){
                new->link = cur->link;             // 새 노드의 다음 노드에 기준 노드의 다음 노드를 지정
                cur->link = new;                   // 기준 노드의 다음 노드에 새 노드를 지정
            }
            cur = cur->link;
            cnt++;
        }
    }
    
}

// 기준 노드의 다음 노드를 삭제하는 함수
void delete(struct NODE *head, int data){
    
    NODE* cur = head;
    NODE* pre = cur;
    
    while(cur->data != data){
        pre = cur;
        cur = cur->link;
    }
    
    pre->link = cur->link;          // 기준 노드의 다음 노드에 삭제할 노드의 다음 노드를 지정
    free(cur);                      // 노드 메모리 해제
    
}

void reverse(NODE * head){
    NODE *p, *q, *r;
    p = head->link;
    q=NULL;
    
    while(p!=NULL){
        r=q;
        q=p;
        p=p->link;
        q->link=r;
    }
    head->link = q;
}

void print_list(NODE* head){
    NODE *cur = head->link;
    while(cur!=NULL){
        printf("%d",cur->data);
        cur = cur->link;
    }
    printf("\n");
    free(cur);
}

int main(){
    
        NODE *head = malloc(sizeof(NODE));

        NODE *node1 = malloc(sizeof(NODE));
        head->link = node1;
        node1->data = 10;

        NODE *node2 = malloc(sizeof(NODE));
        node2->data = 20;
        node1->link = node2;
        node2->link = NULL;

        // Initiaized linked list
        printf("Original linked list:        ");
        print_list(head);

        // After insert 30 on index 1 in linked list
        insert(head, 1, 30);
        printf("Ater insert 30 in the list:  ");
        print_list(head);

        // After delete 10 in the linked list
        delete(head, 10);
        printf("After delete 10 in the list: ");
        print_list(head);

        // After reversing the linked_list
        reverse(head);
        printf("After reversing the list:    ");
        print_list(head);
        
        return 0;

    
}
