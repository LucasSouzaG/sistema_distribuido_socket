# Netune - Sistemas Distribuídos

**Autores**
- Fernando Albuquerque
- Igor Bertolacio
- Lucas Souza
- Nicolas Gonçalves
- Nicolas Perejon
- Vinicius Abe

## Sobre o Projeto
O _Netune Project_ tem por objetivo ser um estudo de caso sobre sistemas distribuídos. Neste repositório serão encontrados diferentes pequenos sistemas escritos em diferentes linguagens que demonstram a versatilidade da utilização de sistemas distribuídos.

#### O que é um sistema distribuído?
Um sistema distribuído é um conjunto de componentes de software e hardware interconectados que trabalham juntos para realizar uma tarefa ou oferecer um serviço. Nesse tipo de sistema, múltiplos computadores ou dispositivos estão ligados em rede e colaboram entre si para alcançar um objetivo comum.

A principal característica de um sistema distribuído é que os componentes individuais são autônomos e independentes, mas podem se comunicar e coordenar suas ações para realizar tarefas complexas. Essa descentralização permite que o processamento, armazenamento e controle sejam distribuídos entre os diferentes nós do sistema, em vez de estarem concentrados em uma única máquina central.

Os sistemas distribuídos podem variar em tamanho e escala, desde pequenos sistemas locais até grandes infraestruturas distribuídas globalmente. Eles são amplamente utilizados em várias áreas, como redes de computadores, sistemas de gerenciamento de banco de dados distribuídos, serviços em nuvem, redes sociais, sistemas de comércio eletrônico e muito mais.

Alguns dos benefícios dos sistemas distribuídos incluem a escalabilidade, pois é possível adicionar mais nós para lidar com maior carga de trabalho; a tolerância a falhas, já que a falha de um nó não leva à falha completa do sistema; e o desempenho aprimorado, pois as tarefas podem ser executadas em paralelo.

No entanto, os sistemas distribuídos também apresentam desafios, como a complexidade da coordenação entre os nós, a sincronização de dados e a segurança, que precisam ser abordados para garantir um funcionamento eficiente e confiável do sistema.

#### O Estudo de Caso - Sistema de Chamadas
Um sistema de chamadas para uma faculdade pode se beneficiar do uso de sistemas distribuídos para melhorar sua eficiência e confiabilidade. Vou descrever detalhadamente como um sistema distribuído poderia ser implementado nesse contexto.

##### Arquitetura Distribuída:

- O sistema seria composto por vários nós distribuídos em diferentes locais dentro da faculdade, diferentes salas de aula.
- Cada nó seria um dispositivo de comunicação, como um celular, um computador com software de chamadas ou até mesmo um aplicativo móvel específico para o sistema.
- Os nós estariam interconectados por uma rede de comunicação, como uma rede local (LAN) ou uma rede de área ampla (WAN).
- Poderia haver um servidor centralizado que atuaria como ponto de controle e coordenação do sistema, mas também seria possível adotar uma abordagem descentralizada com vários servidores distribuídos.

##### Funcionalidades do Sistema:
- Realização de chamadas: Os usuários poderiam realizar chamadas em sala de aula dentro da faculdade para outros alunos, discando números de extensão ou utilizando diretórios de contatos.
- Identificação de chamadas: O sistema poderia exibir informações sobre o professor, como nome, matéria dada e horário da aula, com base em um banco de dados centralizado ou distribuído.
  
##### Distribuição de Carga
- O sistema poderia ser projetado para distribuir a carga de chamadas de forma equilibrada entre os nós, a fim de evitar sobrecarga e garantir um desempenho adequado.
- Poderiam ser implementados algoritmos de balanceamento de carga para distribuir as chamadas com base na capacidade de processamento de cada nó, minimizando gargalos e otimizando o uso dos recursos disponíveis.

##### Tolerância a Falhas
- Um sistema distribuído permite maior tolerância a falhas, pois a falha de um nó não afetaria o funcionamento geral do sistema.
- Em caso de falha de um nó, as chamadas da sala poderiam ser automaticamente redirecionadas para outros nós disponíveis, garantindo a continuidade do serviço.
- Além disso, poderiam ser implementados mecanismos de monitoramento e detecção de falhas para identificar e lidar com problemas rapidamente.

##### Segurança
- O sistema de chamadas para a faculdade deve considerar aspectos de segurança para proteger as informações e a privacidade dos usuários.
- Seriam necessários mecanismos de autenticação para garantir que apenas usuários autorizados possam realizar chamadas ou acessar recursos do sistema.

##### Integração com outros Sistemas
- O sistema de chamadas poderia ser integrado a outros sistemas utilizados na faculdade, como o sistema de gerenciamento acadêmico.
- Por exemplo, os dados dos alunos poderiam ser sincronizados com o sistema de chamadas, permitindo identificar o nome e a localização de um aluno quando ele fizer uma chamada.

Em resumo, um sistema de chamadas para uma faculdade utilizando sistemas distribuídos ofereceria vantagens como escalabilidade, tolerância a falhas e desempenho aprimorado. Além disso, proporcionaria uma infraestrutura flexível e modular, permitindo futuras expansões e integrações com outros sistemas utilizados na instituição.