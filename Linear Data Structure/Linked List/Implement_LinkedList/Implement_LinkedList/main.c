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
    struct NODE* next;    // 다음 노드의 주소를 저장할 포인터(자기참조 구조체 포인터) : "노드 구조체의 주소" 저장
    
    
}node;

//n번째 노드에 저장되어 있는 값을 불러오는 함수
char get(struct NODE *target,int n){
    
    for(int i=0;i<n;i++){
        target=target->next;
    }
    return target->data;
}

// 기준 노드 뒤에 노드를 추가하는 함수
void insertNode(struct NODE *target, int data){
    
    node* newNode = (node*)malloc(sizeof(node));    // new node
    newNode->next = target->next;                   // 새 노드의 다음 노드에 기준 노드의 다음 노드를 지정
    newNode->data = data;                           // 데이터 저장
    target->next = newNode;                         // 기준 노드의 다음 노드에 새 노드를 지정
    
}

// 기준 노드의 다음 노드를 삭제하는 함수
void deleteFirst(struct NODE *target){
    
    node* deleteNode = target->next;     // 기준 노드의 다음 노드 주소를 저장
    target->next = deleteNode->next;     // 기준 노드의 다음 노드에 삭제할 노드의 다음 노드를 지정
    free(deleteNode);    // 노드 메모리 해제
}

int main(){
    
    node *head = (node*)malloc(sizeof(node));    // head 노드 생성
    // head 노드는 데이터를 저장하지 않음
    
    head->next = NULL;
    
    insertNode(head, 10);                         // head 노드 뒤에 새 노드 추가
    insertNode(head, 20);                         // head 노드 뒤에 새 노드 추가
    insertNode(head, 30);                         // head 노드 뒤에 새 노드 추가

    deleteFirst(head);                          // head 노드 뒤에 있는 노드를 삭제

    node* curr = head->next;                    // 순회용 node 생성 : 연결 리스트 순회용 포인터에 첫 번째 노드의 주소 저장
    while (curr != NULL){                       // 포인터가 NULL이 아닐 때 계속 반복
        printf("%d\n", curr->data);             // 현재 노드의 데이터 출력
        curr = curr->next;                      // 포인터에 다음 노드의 주소 저장
    }
    
    printf("%d\n", get(head,1));
    printf("%d\n", get(head,2));
    
    while (curr != NULL){                       // 포인터가 NULL이 아닐 때 계속 반복
        node *next = curr->next;                // 현재 노드의 다음 노드 주소를 임시로 저장
        free(curr);                             // 현재 노드 메모리 해제
        curr = next;                            // 포인터에 다음 노드의 주소 저장
    }

    free(head);                                 // head 노드 메모리 해제

    return 0;
}
